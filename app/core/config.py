import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "Text Analysis Service"
    APP_VERSION: str = "0.1.0"
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:5173")
    MAX_UPLOAD_SIZE_MB: int = 10


settings = Settings()
