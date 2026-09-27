# Week 03 — Day 05: Database Integration

follow this link for detailed explaination :- [https://medium.com/@ramanbazhanau/mastering-sqlalchemy-a-comprehensive-guide-for-python-developers-ddb3d9f2e829]

## Points Covered

* What is a database?
* Why APIs need databases
* PostgreSQL
* SQL vs NoSQL
* SQLAlchemy
* ORM
* Database connection
* Database engine
* Database session
* Database models
* Tables and columns
* Creating database tables
* CRUD with a database
* Dependency injection for database sessions
* FastAPI + PostgreSQL architecture
* Database integration in AI applications
* Common mistakes
---

# 1. What is a Database?

A **database** is a system used to store, organize, and retrieve data.

For example, an AI Course Support application may store:

```text
Courses
Users
Recommendations
Conversations
```

Instead of storing data temporarily in Python lists:

```python
courses = []
```

we can store it permanently in a database.

---

# 2. Why Do APIs Need Databases?

APIs often need to store data that should remain available after the application restarts.

Without a database:

```text
Application starts
      ↓
Data stored in memory
      ↓
Application stops
      ↓
Data is lost
```

With a database:

```text
Application starts
      ↓
Database
      ↓
Existing data is available
```

---

# 3. PostgreSQL

**PostgreSQL** is a relational database management system.

It stores data in tables.

Example:

```text
courses

id | name      | level
---|-----------|----------
1  | Python    | beginner
2  | FastAPI   | beginner
3  | LangGraph | advanced
```

PostgreSQL supports:

* Relational data
* SQL queries
* Transactions
* Constraints
* Indexes
* Large applications

---

# 4. SQL

**SQL (Structured Query Language)** is used to communicate with relational databases.

Read data:

```sql
SELECT * FROM courses;
```

Insert data:

```sql
INSERT INTO courses (name, level)
VALUES ('FastAPI', 'beginner');
```

Update data:

```sql
UPDATE courses
SET level = 'intermediate'
WHERE id = 2;
```

Delete data:

```sql
DELETE FROM courses
WHERE id = 2;
```

---

# 5. SQL vs NoSQL

### SQL Databases

Examples:

```text
PostgreSQL
MySQL
SQLite
```

They generally store structured data in tables.

### NoSQL Databases

Examples:

```text
MongoDB
Redis
DynamoDB
```

They use different data models depending on the database.

For this week, the focus is **PostgreSQL**.

---

# 6. What is SQLAlchemy?

**SQLAlchemy** is a Python library used to interact with SQL databases.

It allows Python code to work with database objects.

Example:

```python
course = Course(
    name="FastAPI",
    level="beginner"
)
```

SQLAlchemy can translate database operations into the required SQL.

---

# 7. What is ORM?

**ORM (Object-Relational Mapping)** maps objects in a programming language to tables in a relational database.

```text
Python Class
     ↓
Database Table

Course
     ↓
courses
```

Python object:

```python
course = Course(
    name="FastAPI",
    level="beginner"
)
```

Database table:

```text
courses

id | name    | level
---|---------|----------
1  | FastAPI | beginner
```

ORM allows us to work with database data using Python objects.

---

# 8. SQLAlchemy ORM Model

A database model represents a database table.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)
```

Here:

```text
Course
→ Python class

courses
→ Database table

id
→ Column

name
→ Column

level
→ Column
```

---

# 9. Primary Key

A **primary key** uniquely identifies each row in a table.

```text
id | name
---|---------
1  | Python
2  | FastAPI
3  | LangGraph
```

Here, `id` is the primary key.

In SQLAlchemy:

```python
id = Column(Integer, primary_key=True)
```

---

# 10. Database Engine

A **database engine** manages the connection between the application and the database.

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/course_db"

engine = create_engine(DATABASE_URL)
```

The connection URL contains information such as:

```text
Database type
User
Password
Host
Database name
```

Sensitive values should be stored in environment variables instead of directly in the code.

---

# 11. Database Session

A **database session** is used to communicate with the database during a unit of work.

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
```

Create a session:

```python
db = SessionLocal()
```

A session can be used to:

```text
Add data
Read data
Update data
Delete data
Commit changes
```

---

# 12. Creating Database Tables

After defining the models, SQLAlchemy can create the tables:

```python
Base.metadata.create_all(bind=engine)
```

This creates the tables represented by the models.

For larger production applications, migration tools such as **Alembic** are commonly used.

---

# 13. Database Project Structure

A simple FastAPI project can be organized as:

```text
app/
│
├── main.py
├── database.py
│
├── models/
│   └── course.py
│
├── schemas/
│   └── course.py
│
├── routes/
│   └── courses.py
│
└── services/
    └── course_service.py
```

Responsibilities:

```text
main.py
→ FastAPI application

database.py
→ Database connection and session

models/
→ Database models

schemas/
→ Request/response models

routes/
→ API endpoints

services/
→ Business logic
```

---

# 14. Database Model vs Pydantic Model

These models have different purposes.

### SQLAlchemy Model

Represents database data.

```python
class Course(Base):
    ...
```

### Pydantic Model

Validates API input/output.

```python
class CourseCreate(BaseModel):
    name: str
    level: str
```

Remember:

```text
Pydantic
→ API validation

SQLAlchemy
→ Database interaction
```

They are not the same thing.

---

# 15. Database Dependency in FastAPI

FastAPI can provide a database session to a route using a dependency.

```python
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

Use it in a route:

```python
@app.get("/courses")
def get_courses(
    db: Session = Depends(get_db)
):
    ...
```

FastAPI provides the database session to the route.

---

# 16. Why Use `yield` in `get_db()`?

The database session should be closed after the request finishes.

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

Flow:

```text
Create session
      ↓
Give session to route
      ↓
Route finishes
      ↓
Close session
```

This prevents unnecessary database connections from remaining open.

---

# 17. Create Data

Create a course:

```python
course = Course(
    name="FastAPI",
    level="beginner"
)

db.add(course)
db.commit()
db.refresh(course)
```

Meaning:

```text
db.add()
→ Add object to session

db.commit()
→ Save changes to database

db.refresh()
→ Get updated database values
```

After committing, the database may generate an ID:

```text
id = 1
```

---

# 18. Read Data

Get all courses:

```python
courses = db.query(Course).all()
```

Get one course:

```python
course = db.query(Course).filter(
    Course.id == course_id
).first()
```

Flow:

```text
API Request
    ↓
Route
    ↓
Database Session
    ↓
Query
    ↓
Database
    ↓
Result
    ↓
Response
```

---

# 19. Update Data

Find the course:

```python
course = db.query(Course).filter(
    Course.id == course_id
).first()
```

Modify it:

```python
course.name = "Advanced FastAPI"

db.commit()
db.refresh(course)
```

Flow:

```text
Find record
    ↓
Modify object
    ↓
Commit
    ↓
Database updated
```

---

# 20. Delete Data

Find the course:

```python
course = db.query(Course).filter(
    Course.id == course_id
).first()
```

Delete it:

```python
db.delete(course)
db.commit()
```

The record is removed from the database.

---

# 21. CRUD With Database

### Create

```text
POST /courses
      ↓
db.add()
      ↓
db.commit()
```

### Read

```text
GET /courses
      ↓
db.query()
      ↓
Return data
```

### Update

```text
PUT /courses/{id}
      ↓
Find record
      ↓
Modify
      ↓
db.commit()
```

### Delete

```text
DELETE /courses/{id}
      ↓
Find record
      ↓
db.delete()
      ↓
db.commit()
```

---

# 22. Using Pydantic With Database

A real API should use Pydantic models for request validation.

```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    level: str
```

Then:

```python
@app.post("/courses")
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        level=course.level
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course
```

Flow:

```text
JSON Request
     ↓
Pydantic Model
     ↓
Validation
     ↓
SQLAlchemy Model
     ↓
Database
```

---

# 23. FastAPI + PostgreSQL Architecture

The architecture becomes:

```text
Client
   ↓
FastAPI Route
   ↓
Pydantic Request Model
   ↓
Service Layer
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
SQLAlchemy
   ↓
Pydantic Response Model
   ↓
Client
```

Each component has a separate responsibility.

---

# 24. Database Integration in AI Applications

AI applications also need persistent data.

For an **AI Course Support API**, PostgreSQL can store:

```text
Users
Courses
User Profiles
Course History
Recommendations
Conversations
```

Example:

```text
User
 ↓
FastAPI
 ↓
Database
 ↓
User Information
 ↓
LLM
 ↓
Recommendation
```

---

# 25. Database + RAG

An AI application may use different databases for different purposes.

```text
PostgreSQL
→ Application data

Vector Database
→ Embeddings and semantic search
```

Example:

```text
User Data
     ↓
PostgreSQL

Course Documents
     ↓
Embedding Model
     ↓
Vector Database
```

Both can be used by the same AI application.

---

# 26. PostgreSQL in Agentic AI

Agentic applications often need persistent state.

For example:

```text
Agent
 ↓
User Information
 ↓
PostgreSQL
```

```text
Agent
 ↓
Conversation History
 ↓
PostgreSQL
```

```text
Agent
 ↓
Task Information
 ↓
PostgreSQL
```

A possible architecture is:

```text
FastAPI
   ↓
Agent
   ├── LLM
   ├── Tools
   ├── RAG
   ├── Memory
   └── PostgreSQL
```

---

# 27. Common Mistakes

### 1. Hardcoding database credentials

Avoid:

```python
DATABASE_URL = "postgresql://admin:password123@localhost/db"
```

Use environment variables instead.

### 2. Forgetting to close sessions

Use:

```python
try:
    yield db
finally:
    db.close()
```

### 3. Confusing Pydantic and SQLAlchemy models

```text
Pydantic
→ API validation

SQLAlchemy
→ Database
```

### 4. Forgetting `commit()`

```python
db.add(course)
db.commit()
```

### 5. Putting database logic everywhere

Keep database operations organized as the application grows.

### 6. Putting database operations directly in every route

For larger applications, use a service layer to keep routes clean.

---