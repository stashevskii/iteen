import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.tg_token = os.getenv("TG_TOKEN")


config = Config()
