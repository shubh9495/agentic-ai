# Week 03 — Day 06: Authentication & API Security

## Points Covered

* Authentication
* Authorization
* Authentication vs authorization
* Why APIs need authentication
* Password hashing
* JWT
* Access tokens
* JWT structure
* Login flow
* Protected routes
* FastAPI authentication
* OAuth2 password flow
* `OAuth2PasswordBearer`
* Token validation
* Role-based access
* API security basics
* Environment variables and secrets
* Common authentication mistakes
* Authentication in AI applications

---

# 1. What is Authentication?

**Authentication** is the process of verifying who a user is.

In simple words:

> Authentication answers: **"Who are you?"**

Example:

```text
User enters email + password
        ↓
Server verifies credentials
        ↓
User authenticated
```

Common methods include:

* Username/password
* JWT tokens
* OAuth
* API keys
* Session-based authentication
* Multi-factor authentication

---

# 2. What is Authorization?

**Authorization** determines what an authenticated user is allowed to access or perform.

In simple words:

> Authorization answers: **"What are you allowed to do?"**

Example:

```text
User
 ↓
Authenticated?
 ↓
Yes
 ↓
Is user an admin?
 ↓
Yes
 ↓
Allow admin operation
```

---

# 3. Authentication vs Authorization

| Authentication      | Authorization                          |
| ------------------- | -------------------------------------- |
| Verifies identity   | Verifies permissions                   |
| Who are you?        | What can you access?                   |
| Happens first       | Happens after authentication           |
| Login is an example | Role/permission checking is an example |

Flow:

```text
Login
 ↓
Authentication
 ↓
User identified
 ↓
Authorization
 ↓
Check permissions
```

---

# 4. Why Do APIs Need Authentication?

Authentication protects resources that should not be publicly accessible.

Examples:

* User accounts
* Personal data
* Private APIs
* Admin operations
* AI conversations
* User-specific recommendations
* Database operations

For example:

```text
GET /users/123
```

The API should verify whether the requester is allowed to access the resource.

---

# 5. Basic Login Flow

A common login flow:

```text
User
 ↓
Email + Password
 ↓
POST /login
 ↓
Server
 ↓
Verify credentials
 ↓
Generate access token
 ↓
Return token
 ↓
Client
```

Future requests:

```text
Client
 ↓
Access Token
 ↓
API
 ↓
Validate Token
 ↓
Allow Request
```

---

# 6. Password Hashing

Passwords should **never be stored as plain text**.

Bad:

```text
email: user@example.com
password: mypassword123
```

Instead:

```text
Password
   ↓
Hashing algorithm
   ↓
Password hash
   ↓
Database
```

The original password should not be stored in the database.

---

# 7. Hashing vs Encryption

### Hashing

Hashing is generally one-way.

```text
Password
   ↓
Hash
```

The original password is not supposed to be recovered from the hash.

### Encryption

Encryption is designed to be reversible with the appropriate key.

```text
Data
 ↓
Encryption
 ↓
Encrypted data
 ↓
Decryption
 ↓
Original data
```

Passwords should be stored using password hashing rather than reversible encryption.

---

# 8. Password Verification

During login:

```text
Entered Password
       ↓
Hash verification
       ↓
Compare with stored hash
       ↓
Valid / Invalid
```

The server does not need to decrypt the stored password.

A password-hashing library handles the verification process.

---

# 9. What is a Token?

A **token** is a piece of data that represents authenticated access to an application or API.

After successful login:

```text
User
 ↓
Login
 ↓
Server
 ↓
Access Token
```

The client sends the token with future requests:

```http
GET /profile
Authorization: Bearer <token>
```

---

# 10. What is JWT?

**JWT (JSON Web Token)** is a commonly used token format for transmitting claims between systems.

A JWT generally contains:

```text
Header
Payload
Signature
```

Conceptually:

```text
HEADER.PAYLOAD.SIGNATURE
```

---

# 11. JWT Header

The header contains information about the token.

Example:

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

* `alg` → signing algorithm
* `typ` → token type

---

# 12. JWT Payload

The payload contains claims.

Example:

```json
{
    "sub": "123",
    "role": "user"
}
```

Common claims include:

```text
sub → Subject / user identifier
exp → Expiration time
iat → Issued-at time
```

Do not put sensitive information such as passwords or private secrets inside the JWT payload.

---

# 13. JWT Signature

The signature helps verify that the token was created by a trusted party and has not been modified.

Conceptually:

```text
Header
+
Payload
+
Secret / Signing Key
      ↓
Signature
```

The server can verify the signature when it receives the token.

---

# 14. JWT Is Signed, Not Encrypted

A normal JWT is generally **signed, not encrypted**.

Therefore, the JWT payload should not be treated as secret storage.

Do not put information such as:

```text
Passwords
Credit card information
Private secrets
```

inside a JWT.

---

# 15. Access Token

An **access token** is a credential used by the client to access protected resources.

```text
Login
 ↓
Access Token
 ↓
GET /profile
Authorization: Bearer <token>
```

The API validates the token before processing the request.

---

# 16. Bearer Token

A common authorization header is:

```http
Authorization: Bearer <access_token>
```

`Bearer` means the client is presenting the token as the credential for the request.

---

# 17. Protected Routes

A **protected route** requires authentication.

Example public route:

```text
GET /courses
```

Example protected route:

```text
GET /profile
```

Flow:

```text
Request
 ↓
Token?
 ↓
Validate token
 ↓
Valid?
 ├── Yes → Continue
 └── No  → 401 Unauthorized
```

---

# 18. HTTP 401 vs 403

### 401 Unauthorized

Usually means authentication credentials are missing or invalid.

Examples:

```text
Missing token
Invalid token
Expired token
```

### 403 Forbidden

Usually means the user is authenticated but does not have permission.

Example:

```text
Normal user
    ↓
Admin-only endpoint
    ↓
403 Forbidden
```

Remember:

```text
401 → Authentication problem
403 → Permission problem
```

---

# 19. OAuth2

**OAuth 2.0** is an authorization framework used to allow applications to access resources securely.

FastAPI provides utilities for working with OAuth2-based authentication flows.

Example:

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
```

---

# 20. OAuth2PasswordBearer

`OAuth2PasswordBearer` is a FastAPI security utility used to extract a bearer token from the `Authorization` header.

Example:

```python
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

@app.get("/profile")
def profile(
    token: str = Depends(oauth2_scheme)
):
    return {"token": token}
```

For:

```http
Authorization: Bearer abc123
```

FastAPI extracts:

```text
abc123
```

and provides it to the route.

---

# 21. Token Validation

Receiving a token is not enough.

The server must validate it.

Typical flow:

```text
Token
 ↓
Verify signature
 ↓
Check expiration
 ↓
Read user identity
 ↓
Check permissions
 ↓
Allow request
```

---

# 22. Authentication Dependency

FastAPI dependencies can keep authentication logic separate from routes.

```python
from fastapi import Depends

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    # Validate token
    # Find user
    return user
```

Protect a route:

```python
@app.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):
    return current_user
```

Now multiple routes can reuse the same authentication dependency.

---

# 23. Role-Based Authorization

Users can have different roles.

For example:

```text
user
admin
instructor
```

Possible permissions:

```text
User
→ View courses

Instructor
→ Create courses

Admin
→ Delete users
```

Flow:

```text
User
 ↓
Authentication
 ↓
Identify role
 ↓
Authorization
 ↓
Check permission
 ↓
Allow / Deny
```

---

# 24. Simple Role Check

Example:

```python
def require_admin(user):
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
```

An admin-only operation can use this check.

---

# 25. Environment Variables and Secrets

Secrets should not be hardcoded.

Avoid:

```python
SECRET_KEY = "my-super-secret-key"
```

Use an environment variable:

```text
SECRET_KEY=your-secret-key
```

Load it in Python:

```python
import os

SECRET_KEY = os.getenv("SECRET_KEY")
```

For local development, a `.env` file can be used.

Make sure `.env` is included in `.gitignore`.

---

# 26. Authentication Flow With Database

A typical authentication system:

```text
User
 ↓
POST /login
 ↓
FastAPI
 ↓
Find user in PostgreSQL
 ↓
Verify password hash
 ↓
Generate JWT
 ↓
Return access token
```

Protected request:

```text
Client
 ↓
Bearer Token
 ↓
FastAPI
 ↓
Validate JWT
 ↓
Identify User
 ↓
Authorization Check
 ↓
Service
 ↓
Database
 ↓
Response
```

---

# 27. Authentication Architecture

A clean project structure:

```text
app/
│
├── main.py
├── database.py
│
├── models/
│   └── user.py
│
├── schemas/
│   └── user.py
│
├── routes/
│   ├── auth.py
│   └── users.py
│
├── services/
│   └── auth_service.py
│
└── security/
    └── auth.py
```

Responsibilities:

```text
routes/auth.py
→ Login/register endpoints

models/user.py
→ Database user model

schemas/user.py
→ Request/response validation

services/auth_service.py
→ Authentication logic

security/auth.py
→ Token and security logic

database.py
→ Database connection
```

---

# 28. API Security Basics

Authentication is only one part of API security.

### Use HTTPS

Protect data while it travels between client and server.

### Validate Input

Never blindly trust user input.

### Protect Secrets

Use environment variables or a secure secrets manager.

### Use Password Hashing

Never store plain-text passwords.

### Set Token Expiration

Access tokens should have an appropriate expiration time.

### Limit Access

Users should only access resources they are authorized to access.

### Handle Errors Carefully

Do not expose internal implementation details in API errors.

---

# 29. Authentication in AI Applications

Authentication is important in AI applications because requests may contain private user data.

Example:

```text
User
 ↓
Login
 ↓
JWT
 ↓
AI Course Support API
```

The API can identify which user is making an AI request.

For example:

```text
POST /recommend

User ID → 123
Goal → Java Backend
```

The application can retrieve:

```text
User profile
Learning history
Previous recommendations
Saved courses
Conversation history
```

The AI system can then use this information.

---

# 30. Authentication + Agentic AI

An agentic application may look like:

```text
User
 ↓
Authentication
 ↓
FastAPI
 ↓
Agent
 ├── LLM
 ├── Tools
 ├── Memory
 ├── RAG
 └── Database
 ↓
Response
```

Authentication helps ensure that the agent operates within the correct user's access boundaries.

For example:

```text
User A
 ↓
Agent
 ↓
User A's private data
```

The agent should not accidentally access User B's private data.

---

# 31. Common Mistakes

### 1. Storing plain-text passwords

Never store passwords directly.

### 2. Hardcoding secrets

Do not commit secret keys to GitHub.

### 3. Putting sensitive information in JWT payloads

JWT payloads should not be treated as private storage.

### 4. Confusing authentication and authorization

```text
Authentication → Who are you?

Authorization → What can you do?
```

### 5. Not checking token expiration

Expired tokens should not remain valid indefinitely.

### 6. Protecting only the frontend

Security checks must happen on the backend.

### 7. Returning detailed internal errors

Avoid exposing database errors, stack traces, or secrets to clients.

---

# 32. Day 06 Interview Questions

### 1. What is authentication?

Authentication verifies the identity of a user.

### 2. What is authorization?

Authorization determines what an authenticated user is allowed to access or perform.

### 3. What is the difference between authentication and authorization?

Authentication determines **who you are**, while authorization determines **what you can do**.

### 4. What is JWT?

JWT is a token format commonly used to transmit claims between systems.

### 5. What are the three parts of a JWT?

```text
Header
Payload
Signature
```

### 6. Is JWT encrypted?

A normal JWT is signed, not encrypted. Its payload should not contain sensitive information.

### 7. What is a bearer token?

A bearer token is a credential sent in the `Authorization` header:

```text
Authorization: Bearer <token>
```

### 8. What is password hashing?

Password hashing converts a password into a one-way hash that can be stored instead of the original password.

### 9. What is the difference between 401 and 403?

```text
401 → Authentication is missing or invalid

403 → User is authenticated but not allowed
```

### 10. What is `OAuth2PasswordBearer`?

It is a FastAPI security utility that extracts a bearer token from the authorization header.

### 11. Why use `Depends()` for authentication?

It allows authentication logic to be reused across multiple protected routes.

### 12. Why should secrets be stored in environment variables?

To prevent sensitive credentials from being exposed in source code or repositories.

---