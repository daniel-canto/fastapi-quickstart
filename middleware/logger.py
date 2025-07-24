from fastapi import Request

# Middleware simples que apenas loga todas as requisições HTTP
async def log_requests(request: Request, call_next):
    print(f"[{request.method}] {request.url}")
    response = await call_next(request)
    return response