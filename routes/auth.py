from fastapi.responses import JSONResponse
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas.auth import UserLoginRequest, UserLoginResponse, UserLoginErrorResponse
from utils.auth.jwt_handler import create_token

router = APIRouter()

@router.post("/auth", 
            responses={
                401: {"model": UserLoginErrorResponse, "Error": "Email ou senha inválidos."}
            },
            response_model=UserLoginResponse, 
            status_code=status.HTTP_201_CREATED)
def login(user: UserLoginRequest, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.email == user.email).first()
    if not user_query:
        return JSONResponse(
            status_code=401,
            content=UserLoginErrorResponse(
                Error="Email  ou senha inválidos.",
            ).dict()
        )
    
    if user_query.email == user.email and user_query.senha == user.senha:
        token = create_token({"sub": user_query.email})
        return {"acess_token": token}
    else:
        return JSONResponse(
            status_code=401,
            content=UserLoginErrorResponse(
                Error="Email  ou senha inválidos.",
            ).dict()
        )

        