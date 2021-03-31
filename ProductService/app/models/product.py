# from sqlalchemy import Column,Integer,Float,String
import sqlalchemy as sa
from sqlalchemy.sql import select,update,insert,delete
from fastapi import HTTPException
from typing import Optional

from ..db import metadata
from ..db import database as db
products=sa.Table(
        "products",
        metadata,
        sa.Column("id",sa.Integer,primary_key=True,index=True,autoincrement=True),
        sa.Column("name",sa.String,nullable=False,unique=True,index=True),
        sa.Column("price",sa.Float,nullable=False),
        sa.Column("quantity",sa.Integer,nullable=False)
    )

class ProductUtility:
    @classmethod
    async def getAll(cls):
        query=products.select()
        allproducts=await db.fetch_all(query)
        return allproducts
    @classmethod
    async def getById(cls,id):
        query=products.select().where(products.columns.id==id)
        product=await db.fetch_one(query)
        return product

    @classmethod
    async def getByAttribute(cls, attribute,value):
        # print(products.columns[attribute].type)

        if isinstance(products.columns[attribute].type,sa.Integer):
            try:
                query = products.select().where(products.columns[attribute] == int(value))
            except:
                raise HTTPException(status_code=400,detail="Invalid value")
        elif isinstance(products.columns[attribute].type,sa.Float):
            try:
                query = products.select().where(products.columns[attribute] == float(value))
            except:
                raise HTTPException(status_code=400, detail="Invalid value")
        else:
            query = products.select().where(products.columns[attribute] == str(value))
        product = await db.fetch_all(query)
        return product

    @classmethod
    async def liveSearch(cls,value:Optional[str]=""):
        likeString="%"+str(value)+"%"
        query=products.select().where(sa.or_(
            sa.cast(products.columns.id,sa.String).ilike(likeString),
            products.columns.name.ilike(likeString),
            sa.cast(products.columns.price,sa.String).ilike(likeString),
            sa.cast(products.columns.quantity,sa.String).ilike(likeString)
        ))
        product=await db.fetch_all(query)
        return product

    @classmethod
    async def create(cls,**product):
        query=products.insert().values(**product)
        productid=await db.execute(query)
        return productid
    @classmethod
    async def update(cls,id,**product):
        query=products.update().where(products.columns.id==id).values(**product)
        product=await db.execute(query)
        return product
    @classmethod
    async def updateByAttribute(cls, attribute:str,value, **product):
        query = products.update()
        if isinstance(products.columns[attribute].type, sa.Integer):
            try:
                query = query.where(products.columns[attribute] == int(value))
            except:
                raise HTTPException(status_code=400, detail="Invalid value")
        elif isinstance(products.columns[attribute].type, sa.Float):
            try:
                query = query.where(products.columns[attribute] == float(value))
            except:
                raise HTTPException(status_code=400, detail="Invalid value")
        else:
            query = query.where(products.columns[attribute] == str(value))
        query=query.values(**product)
        product = await db.execute(query)
        return product
        # query = products.update().where(products.columns.name == name).values(**product)
        # product = await db.execute(query)
        # return product
        # ids=[]
        # for item in forUpdate:
            # ids.append(item.id)

    @classmethod
    async def delete(cls,id):
        query=products.delete().where(products.columns.id==id)
        product=await db.execute(query)
        return product
