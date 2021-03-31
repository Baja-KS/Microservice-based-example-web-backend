from typing import List,Optional
from fastapi import APIRouter,HTTPException
from ..models.product import ProductUtility
from ..schemas.products import ProductIn,Product

productsRouter=APIRouter()

# @productsRouter.get("/",response_model=List[Product])
# async def getAllProducts():
#     allProducts=await ProductUtility.getAll()
#     return [Product(**product).dict() for product in allProducts]
@productsRouter.get("/id/{id}",response_model=Product,tags=['Get by ID'])
async def getProductById(id:int):
    product = await ProductUtility.getById(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**product).dict()
@productsRouter.get("/search",response_model=List[Product],tags=['Live Search'])
async def liveSearchProduct(value:Optional[str]=""):
    products = await ProductUtility.liveSearch(value)
    if not products:
        return []
    return [Product(**product).dict() for product in products]
# @productsRouter.get("/name/{name}",response_model=Product,tags=['Get by name'])
# async def getProductByName(name:str):
#     product=await ProductUtility.getByAttribute("name",name)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return Product(**product[0]).dict()
@productsRouter.post("/",tags=['Create new product'])
async def createProduct(product:ProductIn):
    newProduct=await ProductUtility.create(**product.dict())
    return {"id":newProduct}
@productsRouter.put("/id/{id}",tags=['Find by ID and update'])
async def updateProduct(id:int,newAttributes:ProductIn):
    newProduct=await ProductUtility.update(id,**{k:v for k,v in newAttributes.dict().items() if v is not None})
    # if not newProduct:
    #     raise HTTPException(status_code=404, detail="Product not found")
    return newProduct
# @productsRouter.put("/name/{name}",tags=['Find by name and update'])
# async def updateProduct(name:str,newAttributes:ProductIn):
#     newProduct=await ProductUtility.updateByAttribute("name",name,**{k:v for k,v in newAttributes.dict().items() if v is not None})
#     # if not newProduct:
#     #     raise HTTPException(status_code=404, detail="Product not found")
#     return newProduct
@productsRouter.delete("/id/{id}",tags=['Delete'])
async def deleteProduct(id:int):
    deleted=await ProductUtility.delete(id)
    return deleted