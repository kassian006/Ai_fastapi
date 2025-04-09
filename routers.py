from fastapi import APIRouter, HTTPException, File, UploadFile
from predict import get_predictions

router = APIRouter(prefix='/api', tags=['CheckNumber'])


@router.post('/predict')
async def predict(file: UploadFile = File()):
    try:
        image_bytes = await file.read()
        if not image_bytes:
            raise HTTPException(status_code=400, detail='Файл не правильный')
        result = await get_predictions(image_bytes)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))
