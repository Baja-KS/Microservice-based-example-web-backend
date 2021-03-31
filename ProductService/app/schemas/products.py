from pydantic import BaseModel
from typing import Optional


class ProductIn(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    quantity: Optional[int]=None


class Product(ProductIn):
    id: int


