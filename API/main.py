import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException,Security, Depends
from PIL import Image
import numpy as np
import mlflow.pyfunc
import mlflow
from io import BytesIO
from starlette.status import HTTP_403_FORBIDDEN
from fastapi.security.api_key import APIKeyQuery, APIKey
import imghdr


app = FastAPI()
API_KEY = "grupo4asdfgh"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key_query: str = Security(api_key_query)):

    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )




ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg'}

@app.post("/api/v0/predict")
async def predict(file: UploadFile, api_key: APIKey = Depends(get_api_key)):
    if not file.filename.lower().endswith(('.jpg', '.jpeg')):
        return {"error": "Only .jpg or .jpeg files are allowed."}

    contents = await file.read()

    # Check if the file is an image
    image_type = imghdr.what(None, contents)
    if image_type is None:
        return {"error": "Uploaded file is not a valid image."}

    img = Image.open(BytesIO(contents)).resize((224, 224))
    img_array = np.expand_dims(np.array(img).astype('float32') / 255.0, axis=0)

    mlflow.set_tracking_uri("https://dagshub.com/RicardoHdz12/BrainTumors_CNN.mlflow ")
    logged_model = 'runs:/c4d75f4c60764e2eaba381c821d5eaaa/VGGv2'
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    predictions = loaded_model.predict(img_array)
    class_labels = ['Glioma Tumor', 'Meningioma Tumor', 'Normal', 'Pituitary Tumor']

    predicted_index = np.argmax(predictions)
    predicted_label = class_labels[predicted_index]

    return {"Diagnosis": predicted_label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=False)