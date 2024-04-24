from fastapi import APIRouter, HTTPException
from typing import List
from dto.Statistical_dto import Statistical
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/statistical"
statistical_services = requests.Session()
statistical_services.headers.update({"Content-Type": "application/json"})
statistical_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

@router.get("/{year}")
async def get_statistical_year(year: int):
    response = statistical_services.get(f"{SERVICE_URL}/{year}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/countYear")
async def get_years():
    response = statistical_services.get(f"{SERVICE_URL}/countYear")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/revenue/year/{year}")
async def get_revenue_by_year(year: int):
    response = statistical_services.get(f"{SERVICE_URL}/revenue/year/{year}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/get-all-order-success")
async def get_all_order_success():
    response = statistical_services.get(f"{SERVICE_URL}/get-all-order-success")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/get-category-seller")
async def get_category_best_seller():
    response = statistical_services.get(f"{SERVICE_URL}/get-category-seller")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/get-inventory")
async def get_inventory():
    response = statistical_services.get(f"{SERVICE_URL}/get-inventory")
    if response.raise_for_status():
        return response.status_code
    return response.json()
