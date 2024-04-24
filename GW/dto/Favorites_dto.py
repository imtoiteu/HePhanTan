from pydantic import BaseModel

class Favorite(BaseModel):
    id: int
    email: str
    productId: int