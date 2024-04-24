from pydantic import BaseModel

class Product(BaseModel):
    productId: int
    name: str
    price: float
    category: str
    description: str
