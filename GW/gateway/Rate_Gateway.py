from dto.Rate_dto import Rate
from fastapi import APIRouter, HTTPException
from typing import List
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/rates"
rate_services = requests.Session()
rate_services.headers.update({"Content-Type": "application/json"})
rate_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class Rate(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng Rate
#     # (đánh giá, sản phẩm, v.v.)
#     # Thêm các trường khác nếu cần
#     id: int
#     rating: int
#     comment: str
#     productId: int
#     orderDetailId: int

@router.get("/")
async def get_all_rates():
    url = f"{SERVICE_URL}"
    response = rate_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{orderDetailId}")
async def get_rate_by_order_detail_id(orderDetailId: int):
    url = f"{SERVICE_URL}/{orderDetailId}"
    response = rate_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/product/{productId}")
async def get_rates_by_product_id(productId: int):
    url = f"{SERVICE_URL}/product/{productId}"
    response = rate_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/")
async def create_rate(rate: Rate):
    url = f"{SERVICE_URL}"
    response = rate_services.post(url, json=rate.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/")
async def update_rate(rate: Rate):
    url = f"{SERVICE_URL}"
    response = rate_services.put(url, json=rate.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.delete("/{id}")
async def delete_rate(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = rate_services.delete(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()
