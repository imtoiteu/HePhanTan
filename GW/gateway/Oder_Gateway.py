from dto.Cart_dto import Cart
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List
import requests
from pydantic import BaseModel

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/orders"
order_services = requests.Session()
order_services.headers.update({"Content-Type": "application/json"})
order_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class Cart(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng Cart
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     cartId: int
#     address: str
#     phone: str

class Order(BaseModel):
    # Định nghĩa cấu trúc của đối tượng Order
    # (tên, giá trị, v.v.)
    # Thêm các trường khác nếu cần
    orderId: int
    date: datetime
    amount: float
    address: str
    phone: str
    status: int

@router.get("/")
async def get_all_orders():
    url = f"{SERVICE_URL}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{id}")
async def get_order_by_id(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/user/{email}")
async def get_orders_by_user(email: str):
    url = f"{SERVICE_URL}/user/{email}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/{email}")
async def checkout(email: str, cart: Cart):
    url = f"{SERVICE_URL}/{email}"
    response = order_services.post(url, json=cart.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/cancel/{orderId}")
async def cancel_order(orderId: int):
    url = f"{SERVICE_URL}/cancel/{orderId}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/deliver/{orderId}")
async def deliver_order(orderId: int):
    url = f"{SERVICE_URL}/deliver/{orderId}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/success/{orderId}")
async def success_order(orderId: int):
    url = f"{SERVICE_URL}/success/{orderId}"
    response = order_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()
