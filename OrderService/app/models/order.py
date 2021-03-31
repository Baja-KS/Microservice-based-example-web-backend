from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship, Session
from typing import List
from fastapi import HTTPException

from .orderitem import Item
from ..db import Base
from ..schemas.orderitem import ItemAdd


class Order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    isPending=Column(Boolean,default=True)
    items=relationship("Item",back_populates="order")
    def getItems(self,db:Session):
        return db.query(Item).filter(self.id==Item.orderID).all()
    def addItem(self,item:ItemAdd,db:Session):
        dbItem=Item(name=item.name,quantity=item.quantity,price=item.price,orderID=self.id)
        db.add(dbItem)
        db.commit()
        db.refresh(dbItem)
    def clear(self,db:Session):
        return db.query(Item).filter(Item.orderID == self.id).delete(synchronize_session='evaluate')
    def setPending(self,value:bool,db:Session):
        return db.query(Order).filter(Order.id == self.id).update().values(isPending=value)
    @classmethod
    def all(cls,db:Session,includePending:bool=True,includeDone:bool=True):
        query=db.query(Order)
        if not includeDone:
            query=query.filter(Order.isPending==True)
        if not includePending:
            query = query.filter(Order.isPending==False)
        # print(type(query.all()[0]))
        return query.all()
    @classmethod
    def create(cls,db:Session):
        order=Order(isPending=True)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    @classmethod
    def getById(cls,id:int,db:Session):
        result=db.query(cls).filter(cls.id==id).first()
        if result==None:
            raise HTTPException(status_code=404,detail="Order not found")
        return result

