from pydantic import BaseModel
from datetime import datetime

class Notification(BaseModel):
    id: int
    message: str
    time: datetime
    status: bool
