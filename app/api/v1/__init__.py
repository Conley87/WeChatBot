from fastapi import APIRouter

from .receive import router

v1Router = APIRouter()

v1Router.include_router(router)
