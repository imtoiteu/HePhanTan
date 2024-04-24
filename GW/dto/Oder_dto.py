from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    orderId: int
    date: datetime
    amount: float
    address: str
    phone: str
    status: int


class OrderDetail(BaseModel):
    id: int
    orderId: int
    productId: int
    quantity: int