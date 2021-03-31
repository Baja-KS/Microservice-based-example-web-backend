from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

from .db import Base,engine
from .routes.orders import ordersRouter

while True:
    try:
        Base.metadata.create_all(bind=engine)
        break
    except:
        pass

# app=FastAPI(title="Order Service",openapi_url="/orderservice/openapi.json",docs_url="/orderservice/docs")
app=FastAPI(title="Order Service")
app.include_router(ordersRouter,prefix="/orders",tags=['Orders'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# if __name__ == '__main__':
#     uvicorn.run(app,host="0.0.0.0",port=8001)


