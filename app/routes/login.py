from fastapi import APIRouter
from app.security.auth import crear_token

router = APIRouter(tags=["Login"])

usuario_fake = {
    "username": "admin",
    "password": "1234"
}

@router.post("/login")
def login(username: str, password: str):
    if username == usuario_fake["username"] and password == usuario_fake["password"]:
        token = crear_token({"sub": username})
        return {
            "mensaje": "Login correcto",
            "access_token": token,
            "token_type": "bearer"
        }
    return {"error": "Credenciales incorrectas"}