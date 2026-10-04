from pydantic import BaseModel, Field


class CourseQuestion(BaseModel):
    course_id: int
    question: str = Field(min_length=3, max_length=500)


class RecommendationRequest(BaseModel):
    goal: str = Field(min_length=2, max_length=200)
    level: str = Field(min_length=2, max_length=50)
    technology: str = Field(min_length=2, max_length=50)


class SummarizeRequest(BaseModel):
    course_id: int


class GeneralQuestion(BaseModel):
    question: str = Field(min_length=3, max_length=500)


class AIResponse(BaseModel):
    answer: str