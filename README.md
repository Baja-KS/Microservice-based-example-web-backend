# Microservice based example web backend
An example of microservice-based and docker-containerized web backend app

# Services:
  - Product Service (FastAPI,PostgreSQL)
  - Order Service (FastAPI,PostgreSQL)
# Run:
  - Run `docker-compose up -d` (or `sudo docker-compose up -d`) in the main app directory
  - App will start only after the databases have been created,after few seconds or so if they havent been (if there are no db service volumes)
  - Product Service is on port 8002 -- [Product Service Docs](http://localhost:8002/docs)
  - Order Service is on port 8001 -- [Order Service Docs](http://localhost:8001/docs)
# Migrations:
  - Alembic migration tool used for product and order services
  - Adding new migration script: `(sudo) docker-compose run <servicename (product_service,order_service)>  alembic revision --autogenerate -m "<filename>"`
  - Running migrations : `(sudo) docker-compose run <servicename (product_service,order_service)>  alembic upgrade head`
# TODO:
  - Authentication
  - More services with different frameworks and databases
  - Communication between services where necessary (example:updating product quantity when order is made)

