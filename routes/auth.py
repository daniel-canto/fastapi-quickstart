from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserOut, UserLogin
from utils.auth.jwt_handler import create_token

router = APIRouter()

@router.post("/auth")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.email == user.email).first()
    if not user_query:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")
    
    if user_query.email == user.email and user_query.senha:
        token = create_token({"sub": user_query.email})
        print(user_query.id)
        return{"acess_token": token}
    else:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")

        