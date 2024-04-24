from dto.Favorites_dto import Favorite
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/favorites"
favorites_services = requests.Session()
favorites_services.headers.update({"Content-Type": "application/json"})
favorites_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class Favorite(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng Favorite
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     id: int
#     email: str
#     productId: int

@router.get("/email/{email}")
async def find_by_email(email: str):
    url = f"{SERVICE_URL}/email/{email}"
    response = favorites_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/product/{id}")
async def find_by_product(id: int):
    url = f"{SERVICE_URL}/product/{id}"
    response = favorites_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{productId}/{email}")
async def find_by_product_and_user(productId: int, email: str):
    url = f"{SERVICE_URL}/{productId}/{email}"
    response = favorites_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/email")
async def create_favorite(favorite: Favorite):
    url = f"{SERVICE_URL}/email"
    response = favorites_services.post(url, json=favorite.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.delete("/{id}")
async def delete_favorite(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = favorites_services.delete(url)
    if response.raise_for_status():
        return response.status_code
    return {"message": "Favorite deleted successfully"}
