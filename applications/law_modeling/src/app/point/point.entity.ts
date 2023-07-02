import { Column, Entity, ManyToOne, PrimaryColumn } from "typeorm";
import { Clause } from "../clause/clause.entity";

@Entity()
export class Point {
    @PrimaryColumn()
    id: string

    @Column()
    index: string

    @Column()
    content: string

    @ManyToOne(() => Clause)
    clause: Clause
}