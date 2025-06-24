from fitness.db import SessionLocal
from fitness.models import FitnessClass
from datetime import datetime
import pytz

db = SessionLocal()
if not db.query(FitnessClass).first():
    db.add_all([
        FitnessClass(name="Yoga", date_time=pytz.timezone("Asia/Kolkata").localize(datetime(2025, 6, 22, 7, 0)), instructor="Amy", available_slots=5),
        FitnessClass(name="Zumba", date_time=pytz.timezone("Asia/Kolkata").localize(datetime(2025, 6, 22, 8, 0)), instructor="Jessica", available_slots=3),
        FitnessClass(name="HIIT", date_time=pytz.timezone("Asia/Kolkata").localize(datetime(2025, 6, 22, 9, 0)), instructor="Sara", available_slots=4),
    ])
    db.commit()