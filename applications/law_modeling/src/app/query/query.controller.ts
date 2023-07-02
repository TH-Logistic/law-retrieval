import { Controller, Get, Query } from "@nestjs/common";
import { QueryService } from "./query.service";

@Controller()
export class QueryController {

    constructor(private readonly queryService: QueryService) { }

    @Get("/query")
    async query(@Query('query') query: string) {
        return await this.queryService.query(query);
    }
}