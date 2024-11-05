from fastapi import FastAPI
from app.routers import product
from app.utils.exceptions import NotFound, unicorn_exception_handler

app = FastAPI()

app.include_router(product.router)
app.add_exception_handler(NotFound, unicorn_exception_handler)