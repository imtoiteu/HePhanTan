
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from dto.Cart_dto import Cart

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/cart"
cart_services = requests.Session()
cart_services.headers.update({"Content-Type": "application/json"})
cart_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))



@router.get("/user/{email}")
async def get_cart_user(email: str):
    url = f"{SERVICE_URL}/user/{email}"
    response = cart_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/user/{email}")
async def put_cart_user(email: str, cart: Cart):
    url = f"{SERVICE_URL}/user/{email}"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    response = cart_services.put(url, json=cart.dict(), headers=headers)
    if response.raise_for_status():
        return response.status_code
    return response.json()
