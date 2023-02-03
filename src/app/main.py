from fastapi import FastAPI
from src.app.controllers import hoge_v1

app = FastAPI()
app.include_router(hoge_v1.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
