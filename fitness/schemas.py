from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassOut(BaseModel):
    id : int
    name : str
    date_time : datetime
    instructor : str
    available_slots : int
    class Config:
        from_attributes=True

class BookingIn(BaseModel):
    class_id : int
    client_name : str
    client_email : EmailStr

class BookingOut(BaseModel):
    id : int
    class_id : int
    client_name : str
    client_email : str
    class Config:
        from_attributes=True

