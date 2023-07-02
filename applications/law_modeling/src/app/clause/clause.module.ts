import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { PointModule } from "../point/point.module";
import { ClauseController } from "./clause.controller";
import { Clause } from "./clause.entity";
import { GraphClauseService } from "./services/graph.clause.service";
import { RDBClauseService } from "./services/rdb.clause.service";

@Module({
    imports: [
        TypeOrmModule.forFeature([Clause]),
        PointModule
    ],
    controllers: [ClauseController],
    providers: [RDBClauseService, GraphClauseService],
    exports: [RDBClauseService, GraphClauseService]
})
export class ClauseModule {

}