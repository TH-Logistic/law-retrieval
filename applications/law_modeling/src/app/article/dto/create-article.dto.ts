import { CreateClauseDTO } from "../../clause/dto/create-clause.dto";

export class CreateArticleDto {
    index: number
    title: string
    content: string
    documentId: string
    keyphrases: string[]
    clauses: CreateClauseDTO[] = []
}