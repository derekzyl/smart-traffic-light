from config.config import Config
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

config = Config()


app:FastAPI = FastAPI()



@app.get("/")
async def info() -> JSONResponse:
    return JSONResponse(status_code= status.HTTP_200_OK, content={
        "message": "Hello World"
    })


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.HOST,
        port=config.PORT,
        reload=True,
    )
    





