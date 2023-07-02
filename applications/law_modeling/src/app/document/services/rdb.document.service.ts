import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { Document } from "../document.entity";
import { CreateDocumentDTO } from "../dto/create-document.dto";

@Injectable()
export class RDBDocumentService {
    constructor(
        @InjectRepository(Document)
        private readonly documentRepository: Repository<Document>
    ) { }

    async getDocuments(): Promise<Document[]> {
        return this.documentRepository.find()
    }

    async createDocument(createDocumentDTO: CreateDocumentDTO): Promise<Document> {
        const document = this.documentRepository.create({ ...createDocumentDTO, id: createDocumentDTO.code })
        return await this.documentRepository.save(document)
    }

    async getDocumentById(id: string): Promise<Document | null> {
        return await this.documentRepository.findOneBy({ id: id })
    }

}