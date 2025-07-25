from pydantic import BaseModel, Field, EmailStr

class UserLoginRequest(BaseModel):
    email: EmailStr = Field(..., min_length=1, description="O campo `email` é obrigatório", example="Daniel@example.com")
    senha: str = Field(..., min_length=1, description="O campo `senha` é obrigatório")

class UserLoginResponse(BaseModel):
    acess_token: str = Field(...)
    
class UserLoginErrorResponse(BaseModel):
    Error: str = Field(...)
    