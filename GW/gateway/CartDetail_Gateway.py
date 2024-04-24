from dto.Cart_dto import CartDetail
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/cartDetail"
cart_services = requests.Session()
cart_services.headers.update({"Content-Type": "application/json"})
cart_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class CartDetail(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng CartDetail
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     id: int

@router.get("/cart/{id}")
async def get_cart_details_by_id(id: int):
    url = f"{SERVICE_URL}/cart/{id}"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    response = cart_services.get(url, headers=headers)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{id}")
async def get_one_cart_detail(id: int):
    url = f"{SERVICE_URL}/{id}"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    response = cart_services.get(url, headers=headers)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/")
async def post_cart_detail(cartDetail: CartDetail):
    url = f"{SERVICE_URL}/"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    response = cart_services.post(url, json=cartDetail.dict(), headers=headers)
    response.raise_for_status()
    return response.json()

@router.put("/")
async def put_cart_detail(cartDetail: CartDetail):
    url = f"{SERVICE_URL}/"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    response = cart_services.put(url, json=cartDetail.dict(), headers=headers)
    response.raise_for_status()
    return response.status_code

@router.delete("/{id}")
async def delete_cart_detail(id: int):
    url = f"{SERVICE_URL}/{id}"
    headers = {"Authorization": f"Bearer {token_storage.token}"}
    try:
        response = cart_services.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Successfully deleted!!"}
    except cart_services.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
