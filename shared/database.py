import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("BD_USER")
password = os.getenv("BD_PASSWORD")
host = os.getenv("BD_HOST")

# connection database
SQLACHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{user}"

engine = create_engine(
    SQLACHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()
