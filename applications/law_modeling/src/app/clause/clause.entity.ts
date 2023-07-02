import { Column, Entity, ManyToOne, OneToMany, PrimaryColumn } from "typeorm"
import { Article } from "../article/article.entity"
import { Point } from "../point/point.entity"

@Entity()
export class Clause {
    @PrimaryColumn()
    id: string

    @Column()
    index: number

    @Column()
    content: string

    @ManyToOne(() => Article)
    article: Article

    @OneToMany(() => Point, (point) => point.clause)
    points: Point[]
}