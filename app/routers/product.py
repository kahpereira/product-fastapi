from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dependencies import get_db
from app.models.product import Product as ProductModel
from app.schemas.product import ProductBase, ProductResponse

router = APIRouter()

@router.post('/product/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
  db_product = ProductModel(**product.model_dump())
  
  db.add(db_product)
  await db.commit()
  await db.refresh(db_product)
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product
  
@router.put("/product/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product: ProductResponse, db: AsyncSession = Depends(get_db)):
    db_product = await db.get(ProductModel, product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product
  
@router.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await db.get(ProductModel, product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    await db.delete(db_product)
    await db.commit()
    return None