import { HttpModule } from "@nestjs/axios";
import { Module, OnModuleInit } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { readFile } from "fs";
import { ClauseModule } from "../clause/clause.module";
import { DocumentModule } from "../document/document.module";
import { ArticleController } from "./article.controller";
import { Article } from "./article.entity";
import { RDBArticleService } from "./services/rdb.article.service";
import { CreateArticleDto } from "./dto/create-article.dto";
import { GraphArticleService } from "./services/graph.article.service";

@Module({
    imports: [
        HttpModule,
        TypeOrmModule.forFeature([Article]),
        DocumentModule,
        ClauseModule,
    ],
    controllers: [ArticleController],
    providers: [RDBArticleService, GraphArticleService],
    exports: [RDBArticleService, GraphArticleService]
})
export class ArticleModule { }