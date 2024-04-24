from fastapi import APIRouter, HTTPException
from dto.JwtResponse_dto import JwtResponse
from dto.LoginRequest_dto import LoginRequest
from dto.MessageReponse_dto import MessageResponse
from dto.SignupRequest_dto import SignupRequest
from dto.User_dto import User
from typing import List
import requests

router = APIRouter()

# Token Storage Instance
from dto.token_store import token_storage

SERVICE_URL = "http://localhost:8080/api/auth"
auth_services = requests.Session()
auth_services.headers.update({"Content-Type": "application/json"})
auth_services.mount(SERVICE_URL, requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=5))

@router.get("/")
async def get_all():
    response = auth_services.get(f"{SERVICE_URL}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/{id}")
async def get_one(id: int):
    response = auth_services.get(f"{SERVICE_URL}/{id}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/email/{email}")
async def get_one_by_email(email: str):
    response = auth_services.get(f"{SERVICE_URL}/email/{email}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/")
async def create(user: User):
    response = auth_services.post(f"{SERVICE_URL}", json=user.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/{id}")
async def update(id: int, user: User):
    response = auth_services.put(f"{SERVICE_URL}/{id}", json=user.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.put("/admin/{id}")
async def update_admin(id: int, user: User):
    response = auth_services.put(f"{SERVICE_URL}/admin/{id}", json=user.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.delete("/{id}")
async def delete(id: int):
    response = auth_services.delete(f"{SERVICE_URL}/{id}")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/signin")
async def signin(login_request: LoginRequest):
    response = auth_services.post(f"{SERVICE_URL}/signin", json=login_request.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/signup")
async def signup(signup_request: SignupRequest):
    response = auth_services.post(f"{SERVICE_URL}/signup", json=signup_request.dict())
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.get("/logout")
async def logout():
    response = auth_services.get(f"{SERVICE_URL}/logout")
    if response.raise_for_status():
        return response.status_code
    return response.json()

@router.post("/send-mail-forgot-password-token")
async def send_mail_forgot_password_token(email: str):
    response = auth_services.post(f"{SERVICE_URL}/send-mail-forgot-password-token", data=email)
    if response.raise_for_status():
        return response.status_code
    return response.json()
