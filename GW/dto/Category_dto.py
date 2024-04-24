from enum import Enum
from typing import Optional
from pydantic import BaseModel

class CategoryBestSeller(BaseModel):
    name: str
    count: int
    amount: float


class Category(BaseModel):
    categoryId: int
    categoryName: str
    categoryDescription: str
    # Thêm các trường khác nếu cần   