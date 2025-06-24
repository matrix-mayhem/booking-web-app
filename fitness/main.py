from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from .db import init_db,SessionLocal
from .utils import convert_to_timezone,timezone
from .schemas import ClassOut,BookingIn,BookingOut
from .models import FitnessClass,Booking
from typing import List
import logging

app = FastAPI()
init_db()

logging.basicConfig(level=logging.INFO)
logger= logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/home")
def home_page():
    return {"message" : "Hello User!!!"}

@app.get("/classes",response_model=List[ClassOut])
def list_classes(timeout:str=Query("Asia/Kolkata"),db:Session=Depends(get_db)):
    classes = db.query(FitnessClass).all()
    for cls in classes:
        cls.date_time=convert_to_timezone(cls.date_time,timezone)
        return classes
    
@app.post("/book",response_model=BookingOut)
def book_class(booking:BookingIn,db:Session=Depends(get_db)):
    cls = db.query(FitnessClass).filter(FitnessClass.id==booking.class_id).first()
    if not cls:
        raise HTTPException(status_code=404,details = "Class Not found")
    if cls.available_slots <= 0:
        raise HTTPException(status_code = 400,details = "No slots available")
    cls.available_slots -= 1
    new_booking = Booking(**booking.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    logger.info(f"Booking Confirmed:{booking.client_name} -> class{booking.class_id}")
    return new_booking

@app.get("/bookings",response_model = List[BookingOut])
def get_bookings(email:str,db:Session=Depends(get_db)):
    return db.query(Booking).filter(Booking.client_email==email).all()




