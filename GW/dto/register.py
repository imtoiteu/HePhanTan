from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class Role(int,Enum):
    ADMIN = 1
    STAFF = 2
    CUSTOMERS = 3
    
class RegisForm(BaseModel):
    email: str
    userName: str
    gender: Gender
    password: str
    role: Role

    class Config:
        orm_mode = True
        

class EditPassword(BaseModel):
    id: int
    oldPassword: str
    newPassword: str
    confirmPassword: str
      