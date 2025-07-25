from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import get_db
from models.user import User
from schemas.user import UserCreateRequest, UserResponse, UserErrorResponse

router = APIRouter()

@router.get("/users", 
            responses={
                404: {"model": UserErrorResponse, "Error": "Nenhum usuário encontrado."},
                401: {"model": UserErrorResponse, "Error": "Usuário não autorizado."}
            },
            response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users",
              responses={
                  400: {"model": UserErrorResponse, "Error": "Email já cadastrado."}
              },
              response_model=UserResponse,
              status_code=201)
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        return JSONResponse(
            status_code=400,
            content=UserErrorResponse(
                Error="Email já cadastrado.",
            ).dict()
        )

    new_user = User(name=user.name, email=str(user.email), senha=user.senha)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


