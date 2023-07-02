import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { Clause } from "../clause/clause.entity";
import { CreatePointDTO } from "./dto/create-point.dto";
import { Point } from "./point.entity";

@Injectable()
export class PointService {
    constructor(
        @InjectRepository(Point) private readonly pointRepository: Repository<Point>
    ) {

    }

    createPoints(createPointDTOs: CreatePointDTO[], clause: Clause): Promise<Point[]> {

        const points = this
            .pointRepository
            .create(
                createPointDTOs
                    .map(
                        createPointDTO => ({
                            ...createPointDTO,
                            id: `${createPointDTO.index}|${clause.index}|${clause.article.index}|${clause.article.document.id}`,
                            clause: clause
                        })
                    )
            )

        return this.pointRepository.save(points)

    }
}