from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product as ProductModel
from app.schemas.product import ProductBase, ProductResponse
from app.utils import get_db, commit_and_refresh, NotFound

router = APIRouter()

@router.post('/product/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
  db_product = ProductModel(**product.model_dump())
  
  await commit_and_refresh(db, db_product)
  return db_product

@router.get('/product/', response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_all_products(db: AsyncSession = Depends(get_db)):
  result = await db.execute(select(ProductModel))
  products = result.scalars().all()
  return products

@router.get("/product/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await db.get(ProductModel, product_id)
    if not db_product:
        raise NotFound("Product")
    return db_product
  
@router.put("/product/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product: ProductResponse, db: AsyncSession = Depends(get_db)):
    db_product = await db.get(ProductModel, product_id)
    if not db_product:
        raise NotFound("Product")
    
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    
    await commit_and_refresh(db, db_product)
    return db_product
  
@router.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await db.get(ProductModel, product_id)
    if not db_product:
        raise NotFound("Product")
    
    await db.delete(db_product)
    await db.commit()
    return None