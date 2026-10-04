from pydantic import BaseModel, ConfigDict


class CourseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    level: str
    technology: str
    duration: int
    topics: str
    description: str