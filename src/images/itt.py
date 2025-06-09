from io import BytesIO
import requests
from src.telegram.app.utils.env import config


def image_to_text(b: bytes) -> int | str:
    payload = {
        "apikey": config.ocrapi_token,
        "language": "rus",
    }

    arr = BytesIO(b)
    arr.seek(0)

    response = requests.post(
        "https://api.ocr.space/parse/image",
        files={'filename': ('image.png', arr, 'image/png')},
        data=payload,
    )

    result = response.json()
    if result["IsErroredOnProcessing"]:
        return -1
    return result["ParsedResults"][0]["ParsedText"]
