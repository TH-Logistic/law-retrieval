import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { Article } from "../../article/article.entity";
import { PointService } from "../../point/point.service";
import { Clause } from "../clause.entity";
import { CreateClauseDTO } from "../dto/create-clause.dto";

@Injectable()
export class RDBClauseService {

    constructor(
        @InjectRepository(Clause) private readonly clauseRepository: Repository<Clause>,
        private readonly pointService: PointService,
    ) { }

    createClause(createClauseDTO: CreateClauseDTO, article: Article): Promise<Clause> {
        const clause = this.clauseRepository.create({
            ...createClauseDTO,
            id: `${createClauseDTO.index}|${article.index}|${article.document.id}`,
            article: article
        })

        return this.clauseRepository.save(createClauseDTO)
    }

    async createClauses(createClauseDTOs: CreateClauseDTO[], article: Article): Promise<Clause[]> {

        return Promise.all(createClauseDTOs.map(async (createClauseDTO) => {

            let clause = this.clauseRepository.create({
                ...createClauseDTO,
                id: `${createClauseDTO.index}|${article.index}|${article.document.id}`,
                article: article,
            })

            clause = await this.clauseRepository.save(clause)

            this.pointService.createPoints(createClauseDTO.points, clause)

            return clause
        }))
    }


}