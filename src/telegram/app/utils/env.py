import os
from pathlib import Path

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv(Path(__file__).parent.parent.parent / ".env")
        self.tg_token = os.getenv("TG_TOKEN")
        self.ocrapi_token = os.getenv("OCRAPI_TOKEN")


config = Config()
