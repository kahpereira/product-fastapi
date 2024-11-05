from sqlalchemy import Column, Integer, Numeric, String
from app.database.db import Base

class Product(Base):
  __tablename__ = 'produtos'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(256), nullable=False)
  price = Column(Numeric(10,2), nullable=False)
  description = Column(String(256))