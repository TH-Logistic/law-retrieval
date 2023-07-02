import { ArgumentsHost, Catch, ExceptionFilter, HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { Request, Response } from "express";
import { QueryFailedError, TypeORMError } from "typeorm";

@Catch()
export class CustomExceptionFilter implements ExceptionFilter {
    catch(exception: any, host: ArgumentsHost) {
        const context = host.switchToHttp()
        const request = context.getRequest<Request>();
        const response = context.getResponse<Response>();

        console.log(exception);

        const body = {
            success: false,
            message: "",
            data: null
        }

        if (exception instanceof HttpException) {
            body['message'] = exception.message
        }
        else if (exception instanceof QueryFailedError) {
            body['message'] = exception.message
        }
        else {
            body['message'] = "Internal server error!"
        }

        response
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .json(body);
    }

}