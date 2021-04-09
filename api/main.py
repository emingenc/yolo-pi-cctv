from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import datetime
import uvicorn

app = FastAPI()

db = []

class Image(BaseModel):
    frame: int
    device_name: str
    image_name: str
    image: bytes


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/images")
async def get_images():
    return db

@app.get("/images/{image_id}")
async def get_image(image_id:int):
    image = db[image_id-1]
    return image

@app.post("/images")
async def create_image(image:Image):
    image = image.dict()
    image['time']= datetime.datetime.now()
    db.append(image)
    return db[-1]

@app.delete("/images/{image_id}")
async def delete_image(image_id: int):
    db.pop(image_id-1)
    return {}

if __name__ == "__main__":
    uvicorn.run(app=app,host='0.0.0.0')

