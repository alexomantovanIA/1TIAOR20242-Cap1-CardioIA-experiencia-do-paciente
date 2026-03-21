import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    flask_env: str = os.getenv("FLASK_ENV", "development")
    debug: bool = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port: int = int(os.getenv("PORT", "5000"))
    watson_api_key: str = os.getenv("WATSON_API_KEY", "").strip()
    watson_url: str = os.getenv("WATSON_URL", "").strip().rstrip("/")
    watson_assistant_id: str = os.getenv("WATSON_ASSISTANT_ID", "").strip()
    watson_assistant_version: str = os.getenv(
        "WATSON_ASSISTANT_VERSION", "2021-11-27"
    ).strip()

    @property
    def watson_enabled(self) -> bool:
        return all(
            [self.watson_api_key, self.watson_url, self.watson_assistant_id]
        )


settings = Settings()
