from fastapi import FastAPI
from .db import database,metadata,engine
from .routes.products import productsRouter
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

while True:
    try:
        metadata.create_all(engine)
        break
    except:
        pass

# app=FastAPI(title="Product Service",openapi_url="/productservice/openapi.json",docs_url="/productservice/docs")
app=FastAPI(title="Product Service")
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(productsRouter,prefix="/products")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# if __name__ == '__main__':
#     uvicorn.run(app,host="0.0.0.0",port=8002)