import { INestApplication } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { AppModule } from './app/app.module';
import { CustomExceptionFilter } from './config/filters/exception.filter';
import { ResponseInterceptor } from './config/interceptors/response.interceptor';

async function bootstrap() {
  const app = await createApp();

  configApp(app);
  documentingApp(app)
  runApp(app);
}

async function createApp() {
  return await NestFactory.create(AppModule);
}

async function runApp(app: INestApplication) {
  app.listen(3000);
}

async function configApp(app: INestApplication) {
  app.setGlobalPrefix("/")
  app.useGlobalFilters(new CustomExceptionFilter());
  app.useGlobalInterceptors(new ResponseInterceptor())
}

async function documentingApp(app: INestApplication) {
  const option = new DocumentBuilder()
    .setTitle("Transportation Law Retrieval API")
    .setVersion("0.0.1")
    .setDescription("The API documentation of application.")
    .setContact("thinhlh", "www.hoangthinh.me", "thinhlh0812@gmail.com")
    .setLicense("MIT license", "https://github.com/thinhlh/nestjs-template/blob/main/LICENSE")
    .build();

  const document = SwaggerModule.createDocument(app, option);

  SwaggerModule.setup("/docs", app, document);

}

bootstrap();
