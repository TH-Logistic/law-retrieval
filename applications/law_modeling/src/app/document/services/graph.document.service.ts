import { Injectable } from "@nestjs/common";
import { Neo4jService } from "nest-neo4j/dist";
import { CreateDocumentDTO } from "../dto/create-document.dto";

@Injectable()
export class GraphDocumentService {
    constructor(private readonly neo4jService: Neo4jService) { }

    async createDocument(createDocumentDTO: CreateDocumentDTO) {
        await this.neo4jService.write(
            `
                UNWIND $keyphrases as keyphrase
                MERGE (document: Document {title: toLower($title), code: $code})
                MERGE (key: Keyphrase {content: toLower(trim(keyphrase))})
                MERGE (document)-[:HAS_KEYPHRASE]->(key)
                RETURN document
            `,
            {
                keyphrases: createDocumentDTO.keyphrases,
                title: createDocumentDTO.title,
                code: createDocumentDTO.code
            },);
    }
}