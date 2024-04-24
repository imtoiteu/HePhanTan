from datetime import datetime
from pydantic import BaseModel

class Statistical(BaseModel):
    month: int
    date: datetime
    amount: float
    count: int
