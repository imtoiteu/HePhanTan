from enum import Enum
from typing import Optional
from pydantic import BaseModel

from pydantic import BaseModel
from typing import List

class Cart(BaseModel):
    id: int
    # Thêm các trường khác nếu cần

class CartDetail(BaseModel):
    id: int
    # Thêm các trường khác nếu cần

class CartDetailRequest(BaseModel):
    # Định nghĩa cấu trúc của yêu cầu khi tạo mới hoặc cập nhật chi tiết giỏ hàng
    detail: CartDetail

class CartDetailResponse(BaseModel):
    # Định nghĩa cấu trúc của phản hồi khi lấy thông tin chi tiết giỏ hàng
    detail: CartDetail

class CartDetailsResponse(BaseModel):
    # Định nghĩa cấu trúc của phản hồi khi lấy danh sách các chi tiết giỏ hàng
    details: List[CartDetail]

