from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from utils.auth.jwt_handler import validate_token

# Middleware que exige token Bearer token para acessar rotas protegidas
async def verify_token(request: Request, call_next):
    public_paths = [
        ("/api/v1/auth", "POST"),
        ("/api/v1/users", "POST")
    ]

    for path, method in public_paths:
        if request.url.path == path and request.method == method:
            return await call_next(request)

    if request.url.path.startswith("/api/"):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            # raise HTTPException(status_code=401, detail="Token ausente ou inválido")
            return JSONResponse(
                status_code=401,
                content={"error": "Token expirado ou inválido"}
            )
        
        token = auth_header.split(" ")[1]
        payload = validate_token(token)
        if not payload:
            # raise HTTPException(status_code=401, detail="Token expirado ou inválido")
            return JSONResponse(
                status_code=401,
                content={"error": "Token expirado ou inválido"}
            )

    response = await call_next(request)
    return response