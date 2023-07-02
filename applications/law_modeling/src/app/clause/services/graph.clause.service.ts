import { Injectable } from "@nestjs/common"
import { Neo4jService } from "nest-neo4j/dist"
import { GraphPointService } from "src/app/point/services/graph.point.service";
import { Clause } from "../clause.entity"
import { CreateClauseDTO } from "../dto/create-clause.dto"
import { concatMapTo } from "rxjs";
import { Recoverable } from "repl";

@Injectable()
export class GraphClauseService {

    constructor(
        private readonly neo4jService: Neo4jService,
        private readonly graphPointService: GraphPointService,
    ) { }

    async createClause(createClauseDTO: CreateClauseDTO, articleId: number): Promise<any> {

        const result = await this.neo4jService.write(
            `
            MATCH (article: Article)
            WHERE id(article) = $articleId

            MERGE (clause: Clause {content: $content, index: toInteger($index)})
            MERGE (clause)<-[:HAS_CLAUSE]-(article)

            WITH clause

            FOREACH (keyphrase in $keyphrases | 
                MERGE (key: Keyphrase {content: toLower(trim(keyphrase))})
                MERGE (clause)-[:HAS_KEYPHRASE]->(key)    
                )

            RETURN id(clause) as id
            `,
            {
                keyphrases: createClauseDTO.keyphrases,
                articleId: articleId,
                content: createClauseDTO.content,
                index: createClauseDTO.index,
            });

        for (const record of result.records) {
            for (const point of createClauseDTO.points) {
                await this.graphPointService.createPoint(point, record.get('id').low)
            }
        }
    };
}