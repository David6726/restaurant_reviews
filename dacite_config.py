from datetime import datetime, date
from dacite import Config

def encode_date(dt):
    try:
        return datetime.strptime(dt, '%Y-%m-%d').date()
    except:
        return None
    

config=Config(type_hooks={date: encode_date})