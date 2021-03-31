from sqlalchemy import Column,ForeignKey,Integer,String,Float,Boolean
from sqlalchemy.orm import relationship,Session

from ..db import Base
from ..schemas.orderitem import ItemUpdate

class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String,nullable=False)
    quantity=Column(Integer,default=1)
    price=Column(Float,nullable=False)
    orderID=Column(Integer,ForeignKey("orders.id"))
    order=relationship("Order",back_populates="items")
    def update(self,properties:ItemUpdate,db:Session):
        return db.query(Item).filter(Item.id==self.id).update().values(**{k:v for k,v in properties.dict().items() if v is not None})
    @classmethod
    def removeItemById(cls,id:int,db:Session):
        return db.query(Item).filter(Item.id==id).delete(synchronize_session='evaluate')
