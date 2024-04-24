from typing import Set
from pydantic import BaseModel
from datetime import datetime

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    address: str
    gender: bool
    status: bool
    image: str
    registerDate: datetime
    role: Set[str]
