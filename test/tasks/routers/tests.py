import sys
import os
from fastapi.testclient import TestClient
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.database import Base

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

NEW_TASK = {
    "title": "Test",
    "description": "Description Test",
}

EDIT_TASK = {
    "title": "Title edited",
    "description": "Description edited",
    "completed": True
}

def database_test():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)
	
def create_task():
    database_test()
    return client.post('/tasks', json=NEW_TASK)

def override_get_db():
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()