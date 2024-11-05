from fastapi import Request, status
from fastapi.responses import JSONResponse

class NotFound(Exception):
  def __init__(self, name: str):
        self.name = name

async def unicorn_exception_handler(request: Request, exc: NotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Oops! {exc.name} not found."},
    )