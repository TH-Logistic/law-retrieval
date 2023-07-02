import { Column, Entity, PrimaryColumn, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Document {

    @PrimaryColumn()
    id: string

    @Column({ unique: true })
    title: string
}
