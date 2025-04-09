import requests
import responses
import io
from fastapi import HTTPException
from config import config
from database import client


async def get_predictions(image_bytes: bytes):
    try:
        print('Сурот кетти')
        url= config.ROBOFLOW_URL
        files = {
            'file': ('image.jpg', io.BytesIO(image_bytes), 'image/jpg')
        }
        response = requests.post(url, files=files)
        print(response.text)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail='Ошибка в сервере')

        return {"inference_id": response.json() ['inference_id'],
                'time': response.json()['time'],
                'class': response.json()['predictions'][0]['class'],
                'confidence': response.json()['predictions'][0]['confidence'] * 100}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Ошибкаб {e}')