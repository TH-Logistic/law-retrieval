import { CreateKeyphraseDTO } from "src/app/common/dto/create-keyphrase.dto"

export class CreateDocumentDTO {
    code: string
    title: string
    // keyphrases: CreateKeyphraseDTO[] = []
    keyphrases: string[]
}