from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal

    class Config:
        orm_mode = True

class ProductResponse(ProductBase):
    id: int