import datetime
import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#ADD frontend url to origin for api work.
origins = [
    "http://localhost:5000",
    "http://158.101.214.74", #oracle instance
    "https://158.101.214.74",
    "http://localhost:19007",
    "http://localhost:19006",
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
async def root(request:Request)->dict:
    return {
             "message": "pi-cctv api",
             "swagger_docs": f"{request.client.host+app.docs_url}",
             "redocs": f"{request.client.host+app.redoc_url }",
                                                    }

@app.get("/images")
async def get_images()->list:
    return db

@app.get("/latest")
async def get_latest_images()->list:
    if len(db) > 10:
        return db[-10:][::-1]
    else:
        return db[::-1]

@app.get("/images/{image_id}")
async def get_image(image_id:int)->dict:
    image = db[image_id-1]
    return image

@app.post("/images")
async def create_image(image:Image)->dict:
    image = image.dict()
    image['time']= datetime.datetime.now()
    db.append(image)
    return db[-1]

@app.delete("/images/{image_id}")
async def delete_image(image_id: int)->dict:
    db.pop(image_id-1)
    return {}


if __name__ == "__main__":
    uvicorn.run(app=app,host='0.0.0.0')

