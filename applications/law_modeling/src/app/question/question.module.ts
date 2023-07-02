import { Module } from "@nestjs/common";
import { TypeOrmModule } from "@nestjs/typeorm";
import { Question } from "./question.entity";
import { GraphQuestionService } from "./services/graph.question.service";

@Module({
    imports: [TypeOrmModule.forFeature([Question])],
    providers: [GraphQuestionService],
    exports: [GraphQuestionService]
})
export class QuestionModule {

}