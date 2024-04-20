print("- in modelsBase")
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config
import os


Base = declarative_base()
engine = create_engine(config.SQL_URI_USERS)
DatabaseSession = sessionmaker(bind = engine)


