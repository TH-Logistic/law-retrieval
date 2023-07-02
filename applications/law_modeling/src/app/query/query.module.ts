import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { Neo4jModule } from "nest-neo4j/dist";
import { Article } from "../article/article.entity";
import { Clause } from "../clause/clause.entity";
import { Point } from "../point/point.entity";
import { QueryController } from "./query.controller";
import { QueryService } from "./query.service";

@Module(
    {
        imports: [
            TypeOrmModule.forFeature([Article, Clause, Point]),
        ],
        controllers: [QueryController],
        providers: [QueryService],
    }
)
export class QueryModule {

}