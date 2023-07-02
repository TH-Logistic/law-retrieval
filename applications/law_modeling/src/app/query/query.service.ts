import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Neo4jService } from "nest-neo4j/dist";
import { Repository, Like, ILike } from "typeorm";
import { Article } from "../article/article.entity";
import { RDBArticleService } from "../article/services/rdb.article.service";
import { Clause } from "../clause/clause.entity";
import { Point } from "../point/point.entity";
import { QueryResponse } from "./query.response";

@Injectable()
export class QueryService {

    constructor(
        @InjectRepository(Article) private readonly articleRepository: Repository<Article>,
        @InjectRepository(Clause) private readonly clauseRepository: Repository<Clause>,
        @InjectRepository(Point) private readonly pointRepository: Repository<Point>,
        private readonly neo4jService: Neo4jService,
    ) { }
    async query(queryStr: string) {

        const articles = await this.articleRepository.find({
            where: [
                {
                    title: ILike(`%${queryStr}%`),
                },
                {
                    content: ILike(`%${queryStr}%`)
                },
            ],

        })

        const clauses = await this.clauseRepository.find({
            where: {
                content: ILike(`%${queryStr}%`)
            }
        })

        const points = await this.pointRepository.find({
            where: {
                content: ILike(`%${queryStr}%`),
            }
        })
        const ar = articles.map<QueryResponse>(article => ({ id: article.id, content: article.title }))
        const cl = clauses.map<QueryResponse>(clause => ({ id: clause.id, content: clause.content }))
        const po = points.map<QueryResponse>(point => ({ id: point.id, content: point.content }))

        return ar.concat(cl, po)
    }
}