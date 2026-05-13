from pydantic_settings import BaseSenttings

class Settings(BaseSenttings):
    PROJECT_NAME: str = "AegisNDR"
    DATABASE_URL: str = "sqlite:///aegisndr.db"

    ZEEL_LOG_PATH: str = "data/raw/conn.log"
    SURICATA_LOG_PATH: str = "data/raw/eve.log"

    class Config:
        case_sensitive = True
    
settings = Settings()