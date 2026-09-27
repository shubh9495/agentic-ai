from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    goal: str
    current_skills: list[str]
    experience: str


class Recommendation(BaseModel):
    course: str
    reason: str


class RecommendationResponse(BaseModel):
    goal: str
    recommendations: list[Recommendation]
    next_steps: list[str]