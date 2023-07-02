import { HttpService } from "@nestjs/axios";
import { Body, Controller, Get, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Article } from "./article.entity";
import { RDBArticleService } from "./services/rdb.article.service";
import { CreateArticleDto } from "./dto/create-article.dto";
import { GraphArticleService } from "./services/graph.article.service";

@Controller()
export class ArticleController {

    constructor(
        private readonly articleService: RDBArticleService,
        private readonly graphArticleServide: GraphArticleService,
    ) {

    }

    @Get("/articles")
    async getArticles(@Req() request: Request): Promise<Article[]> {
        const articles = await this.articleService.getArticles();
        return articles;
    }

    @Post("/article")
    async createArticle(@Body() createArticleDTO: CreateArticleDto): Promise<Article> {
        return this.articleService.createArticle(createArticleDTO)
    }

    @Post("/articles")
    async createArticles(@Body() createArticleDTOs: CreateArticleDto[]): Promise<Article[]> {
        return Promise.all(
            createArticleDTOs
                .map(async (createArticleDTO) => await this.createArticle(createArticleDTO))
        )
    }
}