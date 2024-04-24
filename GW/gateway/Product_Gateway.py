from dto.Product_dto import Product
from fastapi import APIRouter, HTTPException
from typing import List
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/products"
product_services = requests.Session()
product_services.headers.update({"Content-Type": "application/json"})
product_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class Product(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng Product
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     productId: int
#     name: str
#     price: float
#     category: str
#     description: str

@router.get("/")
async def get_all_products():
    url = f"{SERVICE_URL}"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/bestseller")
async def get_bestseller_products():
    url = f"{SERVICE_URL}/bestseller"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/bestseller-admin")
async def get_admin_bestseller_products():
    url = f"{SERVICE_URL}/bestseller-admin"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/latest")
async def get_latest_products():
    url = f"{SERVICE_URL}/latest"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/rated")
async def get_rated_products():
    url = f"{SERVICE_URL}/rated"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/suggest/{categoryId}/{productId}")
async def get_suggested_products(categoryId: int, productId: int):
    url = f"{SERVICE_URL}/suggest/{categoryId}/{productId}"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/category/{id}")
async def get_products_by_category(id: int):
    url = f"{SERVICE_URL}/category/{id}"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{id}")
async def get_product_by_id(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = product_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/")
async def create_product(product: Product):
    url = f"{SERVICE_URL}"
    response = product_services.post(url, json=product.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/{id}")
async def update_product(id: int, product: Product):
    url = f"{SERVICE_URL}/{id}"
    response = product_services.put(url, json=product.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.delete("/{id}")
async def delete_product(id: int):
    url = f"{SERVICE_URL}/{id}"
    response = product_services.delete(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()
