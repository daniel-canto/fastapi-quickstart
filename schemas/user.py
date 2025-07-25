from pydantic import BaseModel, Field, EmailStr

class UserCreateRequest(BaseModel):
    # O `...` é usado para declarar obrigatoriedade do campo, enquanto o `example`
    # é usado para a documentação no Swagger.
    name: str = Field(..., min_length=1, description="O campo `name` é obrigatório.", example="Daniel")
    email: EmailStr = Field(..., description="Email válido obrigatório.", example="Daniel@example.com")
    senha: str = Field(..., min_length=1, description="O campo `senha` é obrigatório")

class UserResponse(BaseModel):
    id: int
    name: str = Field(example="Daniel")
    email: EmailStr = Field(example="Daniel@example.com")

    class Config:
        orm_mode = True

class UserErrorResponse(BaseModel):
    Error: str = Field(...)