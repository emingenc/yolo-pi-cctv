from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import datetime
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#ADD frontend url to origin for api work. 
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8081/"
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

