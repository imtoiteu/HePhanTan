from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/orderDetail"
order_detail_services = requests.Session()
order_detail_services.headers.update({"Content-Type": "application/json"})
order_detail_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class OrderDetail(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng OrderDetail
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     id: int
#     orderId: int
#     productId: int
#     quantity: int

@router.get("/order/{id}")
async def get_order_details_by_order_id(id: int):
    url = f"{SERVICE_URL}/order/{id}"
    response = order_detail_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()
