from spacy.lang.vi import Vietnamese
from src.repositories.graph import GraphRepository
from src.config.settings import Settings
from src.schemas.query import QueryOut
from neo4j import Record
from src.dependencies.law_retrieval import LawRetrieval
import spacy
import functools

settings = Settings()
graphRepository = GraphRepository(uri=settings.get_graph_database_url())


def map_record_to_response(record: Record, node_key: str, code_key: str) -> QueryOut:
    node = record.get(node_key)
    node_label = node.labels
    return QueryOut(
        title=node.get("title"),
        content=node.get("content"),
        type=list(node_label)[0],
        code=record.get(code_key),
    )


nlp = spacy.load("vi_core_news_lg")
nlp.add_pipe("textrank")


class QueryService:
    def query_articles(self, query: str) -> list[QueryOut]:
        law_retrieval = LawRetrieval(query)
        doc = nlp(query)
        words = law_retrieval.keyphrases()

        keyphrases = []
        for word in words:
            tag_result = []
            doc = nlp(word)
            for token in doc:
                tag_result.append(token.text + "|" + token.tag_)

                if token.tag_ == "N" or token.tag_ == "V":
                    keyphrases.append(token.text)
        result = []

        for keyphrase in keyphrases:
            query_result = graphRepository.query(
                f"""
                MATCH (n)
                WHERE (n:Point)
                AND toLower(n.content) CONTAINS $query
                WITH n
                MATCH (d: Document)-[:HAS_ARTICLE]-(a:Article)-[:HAS_CLAUSE]-(c:Clause)-[:HAS_POINT]-(n)
                RETURN n, n.index + "_" + c.index + "_" + a.index + "_" + d.code as code
                LIMIT 5
                """,
                parameters={"query": keyphrase},
            )

            query_out = list(
                map(
                    lambda r: map_record_to_response(
                        record=r, node_key="n", code_key="code"
                    ),
                    query_result,
                )
            )

            result.append(query_out)

        result = functools.reduce(lambda a, b: [*a, *b], result)

        question = nlp(query)

        result = sorted(
            list(
                map(
                    lambda n: {
                        "similarity": question.similarity(nlp(n.content.lower())),
                        "node": result,
                    },
                    result,
                )
            ),
            key=lambda a: a["similarity"],
            reverse=True,
        )

        # nodes = list(map(lambda n: n["node"], nodes))
        return result

        # for i in range(len(nodes)):
        #     similarity = question.similarity(nlp(nodes[i].content.lower()))
        #     print(i, question.similarity(nlp(nodes[i].content.lower())))

        # return nodes

        return [
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": "Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác",
            },
            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": "Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:",
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": "Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;",
            },
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": "Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác",
            },
            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": "Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:",
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": "Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;",
            },
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": "Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác",
            },
            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": "Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:",
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": "Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;",
            },
        ]
