import { CreatePointDTO } from "../../point/dto/create-point.dto";

export class CreateClauseDTO {
    index: number
    content: string
    keyphrases: string[] = []
    points: CreatePointDTO[] = []
}