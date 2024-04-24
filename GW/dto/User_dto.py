from pydantic import BaseModel
from typing import Set

class User(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    address: str
    gender: bool
    status: bool
    image: str
    registerDate: str
    role: Set[str]
