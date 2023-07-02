import { Module, OnModuleInit } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { readFile } from "fs";
import { DocumentController } from "./document.controller";
import { Document } from "./document.entity";
import { RDBDocumentService } from "./services/rdb.document.service";
import { CreateDocumentDTO } from "./dto/create-document.dto";
import { GraphDocumentService } from "./services/graph.document.service";

@Module({
    imports: [TypeOrmModule.forFeature([Document])],
    controllers: [DocumentController],
    providers: [RDBDocumentService, GraphDocumentService],
    exports: [RDBDocumentService, GraphDocumentService]

})
export class DocumentModule { }