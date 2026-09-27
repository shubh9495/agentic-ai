from pydantic import BaseModel


class AIQuestion(BaseModel):
    course_id: int
    question: str


class AIResponse(BaseModel):
    answer: str