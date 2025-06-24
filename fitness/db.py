from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

Database_URL = "sqlite:///./bookings.db"
engine = create_engine(Database_URL,connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)