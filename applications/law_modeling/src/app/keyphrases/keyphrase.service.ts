// import { Injectable } from "@nestjs/common";
// import { Neo4jService } from "nest-neo4j/dist";

// enum KeyPhraseOwner {
//     document = "Document",
//     article = "Article",
//     clause = "Clause",
//     point = "Point",
//     question = "Question"
// }

// @Injectable()
// export class KeyphraseService {
//     constructor(private readonly neo4jService: Neo4jService) { }
//     async createKeyphrases(keyphrases: string[], owner: KeyPhraseOwner, ownerId: string) {
//         const result = await this.neo4jService.write(
//             `
//             UNWIND $keyphrases as keyphrase
//             MERGE (key: Keyphrase {content: toLower(trim(keyphrase))})
//             MERGE (owner: $owner) -[:HAS_KEYPHRASE]->(key)
//             RETURN owner
//             UNWIND $keyphrases as keyphrase
//             MERGE (key: Keyphrase {content: toLower(trim(keyphrase))})
//             MERGE (q: Question {no: toInteger($no), content: $content})
//             MERGE (q)-[:HAS_KEYPHRASE]->(key)
//             RETURN q
//         `, {
//             no: no,
//             content: content,
//             keyphrases: keyphrases
//         });
//     }
// }