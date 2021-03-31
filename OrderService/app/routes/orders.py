from typing import List,Optional
from fastapi import APIRouter,HTTPException,Depends
from ..schemas.order import OrderOut
from ..schemas.orderitem import ItemIn,ItemOut,ItemUpdate,ItemAdd
from ..models.order import Order
from ..models.orderitem import Item
from ..db import getDB
from sqlalchemy.orm import Session

ordersRouter=APIRouter()


@ordersRouter.get("/",response_model=List[OrderOut])
def getAllOrders(db:Session=Depends(getDB)):
    return Order.all(db)

@ordersRouter.post("/",response_model=OrderOut)
def createOrder(itemList:List[ItemAdd],db:Session=Depends(getDB)):
    newOrder=Order.create(db)
    # response = httpx.get(url=f"http://localhost:8000/products/name/{item.name}")
    # if len(response.json()) > 0 and response.json()['price'] == item.price:
    for item in itemList:
        newOrder.addItem(item, db)
    return newOrder

@ordersRouter.get("/id/{id}",response_model=OrderOut)
def getOrder(id:int,db:Session=Depends(getDB)):
    return Order.getById(id,db)





