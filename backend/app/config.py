from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://safari:safari_pass@localhost:5432/safari_db"
    class Config:
        env_file = ".env"

settings = Settings()
