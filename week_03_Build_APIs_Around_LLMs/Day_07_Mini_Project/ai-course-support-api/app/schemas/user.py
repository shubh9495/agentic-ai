from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    class Config:#allowing pydantic to take data from objects :- ORM
        from_attributes = True