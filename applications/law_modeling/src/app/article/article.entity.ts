import { Column, Entity, ManyToOne, OneToMany, PrimaryColumn, PrimaryGeneratedColumn } from "typeorm"
import { Clause } from "../clause/clause.entity"
import { Document } from "../document/document.entity"

@Entity()
export class Article {
    @PrimaryColumn()
    id: string

    @Column()
    index: number

    @Column()
    title: string

    @Column()
    content: string

    @ManyToOne(() => Document)
    document: Document

    @OneToMany(() => Clause, (clause) => clause.article)
    clauses: Clause[]
}
