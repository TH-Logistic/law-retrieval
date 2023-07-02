import { Injectable } from "@nestjs/common";
import { Neo4jService } from "nest-neo4j/dist";
import { Question } from "../question.entity";

@Injectable()
export class GraphQuestionService {
    constructor(private readonly neo4jService: Neo4jService) { }

    async createQuestion(question: Question) {
        const result = await this.neo4jService.write(
            `
            UNWIND $keyphrases as keyphrase
            MERGE (key: Keyphrase {content: toLower(trim(keyphrase))})
            MERGE (q: Question {no: toInteger($no), content: $content})
            MERGE (q)-[:HAS_KEYPHRASE]->(key)
            RETURN q
        `, {
            no: question.no,
            content: question.content,
            keyphrases: question.keyphrases
        });
    }
}