from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    id: int
    # O `...` é usado para declarar obrigatoriedade do campo, enquanto o `example`
    # é usado para a documentação no Swagger.
    name: str = Field(..., min_length=1, description="O campo `name` é obrigatório.", example="Daniel")
    email: EmailStr = Field(..., description="Email válido obrigatório.", example="Daniel@example.com")
    senha: str = Field(..., min_length=1, description="O campo `senha` é obrigatório")

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr = Field(..., min_length=1, description="O campo `email` é obrigatório")
    senha: str = Field(..., min_length=1, description="O campo `senha` é obrigatório")