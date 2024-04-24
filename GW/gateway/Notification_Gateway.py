from dto.Notification_dto import Notification
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/notification"
notification_services = requests.Session()
notification_services.headers.update({"Content-Type": "application/json"})
notification_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

# class Notification(BaseModel):
#     # Định nghĩa cấu trúc của đối tượng Notification
#     # (tên, giá trị, v.v.)
#     # Thêm các trường khác nếu cần
#     id: int
#     message: str
#     time: datetime
#     status: bool

@router.get("/")
async def get_all_notifications(offset: int = 0, limit: int = 10):
    params = {"offset": offset, "limit": limit}
    response = notification_services.get(SERVICE_URL, params=params)
    response.raise_for_status()
    return response.json()

@router.post("/")
async def create_notification(notification: Notification):
    url = SERVICE_URL
    response = notification_services.post(url, json=notification.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/readed/{id}")
async def mark_notification_as_read(id: int):
    url = f"{SERVICE_URL}/readed/{id}"
    response = notification_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/read-all")
async def mark_all_notifications_as_read():
    url = f"{SERVICE_URL}/read-all"
    response = notification_services.get(url)
    if response.raise_for_status():
        return response.status_code
    return {"message": "All notifications marked as read successfully"}
