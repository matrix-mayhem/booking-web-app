from datetime import datetime
from pytz import timezone

def convert_to_timezone(dt:datetime,to_tz : str="Asia/Kolkata"):
    try:
        target_tz = timezone(to_tz)
    except Exception:
        target_tz = timezone("Asia/Kolkata")
    return dt.astimezone(target_tz)


