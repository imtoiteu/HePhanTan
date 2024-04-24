from dto.Category_dto import Category
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/categories"
category_services = requests.Session()
category_services.headers.update({"Content-Type": "application/json"})
category_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))



@router.get("/")
async def get_all_categories(offset: int = 0, limit: int = 10):
    params = {"offset": offset, "limit": limit}
    response = category_services.get(SERVICE_URL, params=params)
    response.raise_for_status()
    return response.json()

@router.get("/{id}")
async def get_category_by_id(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = category_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/")
async def create_category(category: Category):
    url = SERVICE_URL
    response = category_services.post(url, json=category.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/{id}")
async def update_category(id: int, category: Category):
    if id != category.categoryId:
        raise HTTPException(status_code=400, detail="ID in path does not match ID in request body")
    url = f"{SERVICE_URL}/{id}"
    response = category_services.put(url, json=category.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.delete("/{id}")
async def delete_category(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = category_services.delete(url)
    if response.raise_for_status():
        return response.status_code
    return {"message": "Category deleted successfully"}
