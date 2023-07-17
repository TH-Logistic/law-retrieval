from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "postgres"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    algorithm: str = 'HS256'
    secret_key: str = 'secret'
    mongo_initdb_host: str = "localhost"
    mongo_initdb_port: int = 27017
    mongo_initdb_database: str = "tplogistic"
    mongo_initdb_root_username: str = "mongo"
    mongo_initdb_root_password: str = "mongo"

    graph_host: str = "localhost"
    graph_port: int = 7687
    graph_user: str = "neo4j"
    graph_db: str = "neo4j"
    graph_password: str = "neo4j"

   # class Config:
   #     env_file = f"../../env/{os.getenv('ENV', 'dev')}.env"

    def get_postgres_database_url(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    def get_mongo_database_url(self):
        return f"mongodb://{self.mongo_initdb_root_username}:{self.mongo_initdb_root_password}@{self.mongo_initdb_host}:{self.mongo_initdb_port}"

    def get_graph_database_url(self):
        return f"bolt://{self.graph_host}:{self.graph_port}"


settings = Settings()
