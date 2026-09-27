from pydantic import BaseModel


class CourseCreate(BaseModel):
    name: str
    level: str
    description: str


class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    description: str

    class Config:
        from_attributes = True