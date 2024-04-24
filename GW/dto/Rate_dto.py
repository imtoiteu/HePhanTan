from pydantic import BaseModel

class Rate(BaseModel):
    id: int
    rating: int
    comment: str
    productId: int
    orderDetailId: int
