from datetime import datetime, timedelta
from jose import JWTError, jwt

# Chave secreta usada para assinar o token (nunca compartilhe isso em produção)
SECRET_KEY = "minha_chave_super_secreta"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("###", payload)
        return payload
    except JWTError:
        print("Saiu")
        return None
