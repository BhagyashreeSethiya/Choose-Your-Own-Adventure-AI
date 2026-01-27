from typing import List 
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_URL : str

    ALLOWED_ORIGINS : str =""

    OPEN_API_KEY: str | None = None

    
    @property
    def allowed_origins_list(self) -> list[str]:
         if self.ALLOWED_ORIGINS: 
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")] 
         return []
    


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()


