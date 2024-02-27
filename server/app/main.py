
from functools import lru_cache

from app.config.config import Config
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse


@lru_cache
def get_config()->Config:
 return Config()


app:FastAPI = FastAPI()



@app.get("/")
async def info() -> JSONResponse:
    return JSONResponse(status_code= status.HTTP_200_OK, content={"message":"welcome to smart traffic light "})
    





