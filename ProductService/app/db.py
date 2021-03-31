import os
import sys

from databases import Database
# from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine

# baseDir=os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(baseDir,".env"))
# sys.path.append(baseDir)


dbUrl=os.getenv("DB_CONN")

engine=create_engine(dbUrl)
metadata=MetaData()

database=Database(dbUrl)