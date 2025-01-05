from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import apiRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)
app.include_router(apiRouter, prefix="/api")
