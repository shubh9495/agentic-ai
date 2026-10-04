from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)        # Beginner / Intermediate / Advanced
    technology = Column(String, nullable=False)   # Python, JavaScript, ...
    duration = Column(Integer, nullable=False)    # hours
    topics = Column(String, nullable=False)       # comma-separated
    description = Column(Text, nullable=False)