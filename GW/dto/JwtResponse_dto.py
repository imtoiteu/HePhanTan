from typing import List
from datetime import date
from pydantic import BaseModel

class JwtResponse(BaseModel):
    token: str
    type: str = "Bearer"
    id: int
    name: str
    email: str
    password: str
    phone: str
    address: str
    gender: bool
    status: bool
    image: str
    registerDate: date
    roles: List[str]

    def __init__(self, accessToken: str, id: int, name: str, email: str, password: str, phone: str,
                 address: str, gender: bool, status: bool, image: str, registerDate: date, roles: List[str]):
        super().__init__(
            token=accessToken,
            id=id,
            name=name,
            email=email,
            password=password,
            phone=phone,
            address=address,
            gender=gender,
            status=status,
            image=image,
            registerDate=registerDate,
            roles=roles
        )
