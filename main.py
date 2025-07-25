from fastapi import FastAPI
from db import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from middleware.logger import log_requests
from middleware.auth import verify_token
from routes import users
from routes import auth

# Instância da aplicação
app = FastAPI(title="API de Usuários com FastAPI", version="1.0")

# Cria tabelas automaticamente se ainda não existirem
Base.metadata.create_all(bind=engine)

# Configuração básica do Middleware de CORS, utilizado para indicar quais
# origens, métodos e cabeçalhos minha API aceitará, de forma global.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_methods=[""],
    allow_headers=[""],
)

# Middlewares de token e logging, em ordem de execução.
app.middleware("http")(verify_token)
app.middleware("http")(log_requests)

# Rotas da API
app.include_router(users.router, prefix="/api/v1", tags=["Usuários"])
app.include_router(auth.router, prefix="/api/v1", tags=["Auth"])
