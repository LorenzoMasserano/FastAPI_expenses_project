from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///database.db"
    APP_NAME: str = "Expense Tracker API"
    SECRET_KEY: str = ""

    model_config = SettingsConfigDict(env_file= ".env")
    
settings = Settings()
