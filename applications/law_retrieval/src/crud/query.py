from src.repositories.graph import GraphRepository
from src.config.settings import Settings
from src.schemas.query import QueryOut
from neo4j import Record

settings = Settings()
graphRepository = GraphRepository(uri=settings.get_graph_database_url())


def map_record_to_response(record: Record, key: str) -> QueryOut:
    node = record.get(key)
    node_label = node.labels
    return QueryOut(
        title=node.get('title'),
        content=node.get('content'),
        type=list(node_label)[0],
        code=node.get('code')
    )


class QueryService:
    def query_articles(self, query: str) -> list[QueryOut]:
        result = graphRepository.query(
            f'''
            MATCH (n) 
            WHERE (n:Article OR n:Clause OR n:POINT)
            AND n.content CONTAINS $query
            RETURN n
            LIMIT 10
            ''',
            parameters={"query": query.lower()}
        )

        return [
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": 'Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác',
            },

            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": 'Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:',
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": 'Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;',
            },
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": 'Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác',
            },

            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": 'Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:',
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": 'Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;',
            },
            {
                "type": "Article",
                "code": "2/NĐ100-2019",
                "title": "Phạm vi điều chỉnh",
                "content": 'Buộc phải thu dọn thóc, lúa, rơm, rạ, nông, lâm, hải sản, rác, chất phế thải, phương tiện, vật tư, vật liệu, hàng hóa, máy móc, thiết bị, biển hiệu, biển quảng cáo, đinh, vật sắc nhọn, dây, các loại vật dụng, vật cản khác',
            },

            {
                "type": "Clause",
                "code": "5-3/NĐ100-2019",
                "title": "",
                "content": 'Các biện pháp khắc phục hậu quả khác trong lĩnh vực giao thông đường bộ:',
            },
            {
                "type": "Point",
                "code": "b-5-2/NĐ100-2019",
                "title": "",
                "content": 'Buộc phải cấp “thẻ nhận dạng lái xe” cho lái xe theo quy định;',
            },

        ]
        return list(map(lambda r: map_record_to_response(r, 'n'), result))
