from fastapi import FastApi, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JsonResponse

from config.config import Config

config = Config()


app:FastApi = FastApi()



@app.get("/")
async def info() -> JsonResponse:
    return JsonResponse(status_code= status.HTTP_200_OK, content={"message":"welcome to smart traffic light "})
    





