import os
import sys

# from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# baseDir=os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(baseDir,".env"))
# sys.path.append(baseDir)
dbUrl=os.getenv("DB_CONN")

engine=create_engine(dbUrl)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def getDB():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


