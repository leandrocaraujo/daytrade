from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from datetime import timedelta
from backend.core.security import (
    create_access_token,
    decode_token,
    get_password_hash,
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    Token,
    TokenData
)

router = APIRouter(prefix="/api/auth", tags=["auth"])
security = HTTPBearer()

# Simulado - em produção usar banco de dados
users_db = {
    "user@example.com": {
        "id": 1,
        "email": "user@example.com",
        "password_hash": get_password_hash("password123"),
        "is_active": True
    }
}

@router.post("/login", response_model=Token)
async def login(email: str, password: str):
    """Endpoint de login"""
    user = users_db.get(email)
    
    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["id"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def get_current_user(credentials: HTTPAuthCredentials = Depends(security)):
    """Retorna informações do usuário atual"""
    token = credentials.credentials
    token_data = decode_token(token)
    
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {"user_id": token_data.user_id, "message": "Autenticado com sucesso"}
