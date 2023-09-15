import base64
import requests
from PIL import Image
from io import BytesIO
from fastapi.exceptions import HTTPException

def decode_base64_to_image(encoding):
    if encoding.startswith("http://") or encoding.startswith("https://"):
        headers = {}
        response = requests.get(encoding, timeout=30, headers=headers)
        try:
            image = Image.open(BytesIO(response.content))
            return image
        except Exception as e:
            raise HTTPException(status_code=500, detail="Invalid image url") from e

    if encoding.startswith("data:image/"):
        encoding = encoding.split(";")[1].split(",")[1]
    try:
        image = Image.open(BytesIO(base64.b64decode(encoding)))
        return image
    except Exception as e:
        raise HTTPException(status_code=500, detail="Invalid encoded image") from e
