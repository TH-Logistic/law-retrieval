// import { CallHandler, ExecutionContext, NestInterceptor } from "@nestjs/common";
// import { catchError, Observable, throwError } from "rxjs";

// export class ErrorResponseInterceptor implements NestInterceptor {
//     intercept(context: ExecutionContext, next: CallHandler<any>): Observable<any> | Promise<Observable<any>> {
//         return next
//             .handle()
//             .pipe(catchError(err => throwError(() => ({
//                 success: false,
//                 message: err.message,
//                 data: null,
//             }))));
//     }

// }