from typing import List,Optional
from pydantic import BaseModel

# __tablename__="items"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name=Column(String,nullable=False)
#     quantity=Column(Integer,default=1)
#     price=Column(Float,nullable=False)
#     orderID=Column(Integer,ForeignKey("orders.id"))
#     order=relationship("Order",back_populates="items")

class __ItemBase(BaseModel):
    name:str
    quantity:int
    price:float
class ItemAdd(__ItemBase):
    pass
class ItemIn(__ItemBase):
    orderID:int

class ItemOut(__ItemBase):
    id:int
    class Config:
        orm_mode = True

class ItemUpdate(BaseModel):
    name:Optional[str]=None
    quantity:Optional[int]=None
    price:Optional[float]=None