from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


#load variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

#session factory

sessionLocal = sessionmaker(
    autocommit = False,
    autoFlush = False,
    bind = engine
)

Base = declarative_base()
