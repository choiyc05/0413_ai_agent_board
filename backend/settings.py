from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  ollama_base_url: str = "http://host.docker.internal:11434"
  ollama_model_name: str = "gemma4:e4b"
  db_host: str = "board-db"
  db_port: int = 3306
  db_database: str = "board"
  db_user: str = "root"
  db_password: str = "1234"

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore"
  )

settings = Settings()
