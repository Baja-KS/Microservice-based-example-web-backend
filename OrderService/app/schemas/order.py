from typing import List,Optional
from pydantic import BaseModel
from ..schemas.orderitem import ItemOut as Item

class OrderOut(BaseModel):
    id: int
    isPending: bool
    items: List[Item] = []
    class Config:
        orm_mode = True
