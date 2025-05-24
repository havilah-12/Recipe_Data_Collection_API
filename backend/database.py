from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

DATABASE_URL = "mysql+pymysql://root:Jo12sam12%40@localhost:3306/recipes_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = sqlalchemy.orm.declarative_base()
