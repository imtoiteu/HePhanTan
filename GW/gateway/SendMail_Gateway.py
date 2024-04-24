from fastapi import APIRouter, HTTPException
import random
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/send-mail"
send_mail_services = requests.Session()
send_mail_services.headers.update({"Content-Type": "application/json"})
send_mail_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

@router.post("/otp")
async def send_opt(email: str):
    random_otp = random.randint(100000, 999999)
    payload = {"email": email}
    response = send_mail_services.post(f"{SERVICE_URL}/otp", json=payload)
    if response.raise_for_status():
        return response.status_code
    return response.json()
