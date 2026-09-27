# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is authentication?
# Answer:
# Authentication verifies the identity of a user.
#
# Clarification:
# Authentication answers "Who are you?" by validating credentials
# such as a username/password pair, an API key, or an SSO/OAuth token.

# Q2. What is authorization?
# Answer:
# Authorization determines what an authenticated user is
# allowed to access or perform.
#
# Clarification:
# Authorization occurs AFTER authentication. Once identity is proven,
# the system evaluates permissions, scopes, or roles (e.g., standard user vs admin).

# Q3. What is the difference between authentication and authorization?
# Answer:
# Authentication answers "Who are you?"
# Authorization answers "What are you allowed to do?"
#
# Clarification:
# Think of an airport: Showing your passport at border control is Authentication.
# Showing your boarding pass to board a specific flight or enter the lounge is Authorization.

# Q4. Why do APIs need authentication?
# Answer:
# Authentication protects resources such as user accounts,
# personal data, private APIs, admin operations, and
# user-specific AI data.
#
# Clarification:
# In Agentic AI backends, unauthenticated access risks exposing proprietary LLM
# endpoints to runaway API billing, malicious prompt injection, or unauthorized access to user vector embeddings.

# Q5. What is password hashing?
# Answer:
# Password hashing converts a password into a one-way hash
# that can be stored instead of the original password.
#
# Clarification:
# Password hashing utilizes cryptographically slow, salted one-way algorithms
# (such as bcrypt or Argon2id). The salt ensures two users with the exact same
# password produce completely different hash strings, defeating rainbow table attacks.

# Q6. What is the difference between hashing and encryption?
# Answer:
# Hashing is generally one-way.
# Encryption is designed to be reversible with the appropriate key.
#
# Clarification:
# - Hashing (one-way): You cannot "decrypt" a hash back into the plaintext password; you only verify guesses.
# - Encryption (two-way): Ciphertext can be decrypted back into plaintext using a private/secret key (e.g., AES-GCM, RSA).

# Q7. What is JWT?
# Answer:
# JWT is a token format commonly used to transmit claims between systems.
#
# Clarification:
# JWT stands for JSON Web Token (RFC 7519). It is compact, URL-safe, and self-contained,
# meaning the token carries user metadata (claims) directly, eliminating the need to query a session database on every request.

# Q8. What are the three parts of a JWT?
# Answer:
# Header
# Payload
# Signature
#
# Clarification:
# A JWT string is composed of three Base64URL-encoded strings separated by dots:
# `header.payload.signature`
# - Header: Algorithm & token type (e.g., {"alg": "HS256", "typ": "JWT"})
# - Payload: Claims and metadata (e.g., {"sub": "123", "exp": 1718000000})
# - Signature: Hash of (Header + Payload) created with your server's SECRET_KEY

# Q9. Is a normal JWT encrypted?
# Answer:
# No. A normal JWT is signed, not encrypted.
# Its payload should not contain sensitive information.
#
# Clarification:
# Base64URL encoding is NOT encryption—anyone with the token can decode and read the payload.
# The signature ensures tamper resistance (integrity), not confidentiality. Never store passwords, API keys, or credit cards in a JWT payload.

# Q10. What is an access token?
# Answer:
# An access token is a credential used by a client to access protected resources.
#
# Clarification:
# Access tokens are typically short-lived (e.g., 15–60 minutes) to minimize the window
# of exposure if intercepted. In modern architectures, they are refreshed using long-lived refresh tokens.

# Q11. What is a bearer token?
# Answer:
# A bearer token is a credential commonly sent using:
# Authorization: Bearer <token>
#
# Clarification:
# The term "bearer" means that whoever possesses ("bears") the token is granted access,
# similar to a physical room key or cash. Because possession equals access, it must be transmitted strictly over HTTPS (TLS).

# Q12. What is the difference between HTTP 401 and 403?
# Answer:
# 401 means authentication is missing or invalid.
# 403 means the user is authenticated but does not have permission.
#
# Clarification:
# - HTTP 401 Unauthorized: "I don't know who you are (missing/expired token)."
# - HTTP 403 Forbidden: "I know who you are, but you do not have permission to touch this resource."

# Q13. What is OAuth2?
# Answer:
# OAuth 2.0 is an authorization framework used to allow
# applications to access resources securely.
#
# Clarification:
# OAuth 2.0 defines standard flows (e.g., Authorization Code Flow, Password Grant)
# enabling third-party apps or clients to access APIs on behalf of a user without sharing their actual password.

# Q14. What is OAuth2PasswordBearer?
# Answer:
# OAuth2PasswordBearer is a FastAPI security utility
# that extracts a bearer token from the Authorization header.
#
# Clarification:
# It serves two purposes:
# 1. Inspects the incoming request's `Authorization: Bearer <token>` header and extracts the raw string.
# 2. Configures FastAPI's Swagger UI (`/docs`) to display the interactive "Authorize" lock button.

# Q15. Why do we use Depends() for authentication?
# Answer:
# Depends() allows authentication logic to be reused
# across multiple protected routes.
#
# Clarification:
# `Depends()` creates a clean security pipeline. It decodes the token, handles errors,
# and injects the `current_user` object directly into your route functions without duplicating validation logic.

# Q16. Why do we use environment variables for secrets?
# Answer:
# To prevent sensitive credentials and keys from being
# exposed in source code or repositories.
#
# Clarification:
# Hardcoding secrets risks leaking them to GitHub or unauthorized team members.
# Use `.env` files locally and environment secrets (like Docker secrets, AWS Secrets Manager, or Doppler) in production.

# Q17. What is role-based authorization?
# Answer:
# Role-based authorization checks a user's role before
# allowing an operation.
# Example:
# user → view courses
# instructor → create courses
# admin → delete users
#
# Clarification:
# Often called RBAC (Role-Based Access Control). Routes enforce requirements either
# via custom dependency functions (e.g., `Depends(require_admin)`) or parameter guards.

# Q18. What should normally be validated in an access token?
# Answer:
# The server should verify the token signature, check
# expiration, identify the user, and check permissions
# when required.
#
# Clarification:
# Standard claims validated:
# - Signature integrity (verifying HMAC with SECRET_KEY)
# - `exp` (Expiration Time): ensures token has not expired
# - `nbf` (Not Before): ensures token is already valid
# - `sub` (Subject): contains the user identifier

# Q19. Why should passwords never be stored as plain text?
# Answer:
# If the database is exposed, plain-text passwords would
# directly reveal user credentials.
#
# Clarification:
# Credential stuffing attacks exploit the fact that users reuse passwords across services.
# A plain-text breach compromises user accounts across the entire internet.

# Q20. Why should security checks happen on the backend?
# Answer:
# Frontend checks can be bypassed.
# The backend must enforce authentication and authorization.
#
# Clarification:
# The client environment (browser/mobile app) is completely under user control.
# Attackers can inspect network requests, forge HTTP headers, or modify frontend JavaScript to bypass UI blocks.

# ============================================================
# CODING PRACTICE
# ============================================================

# ------------------------------------------------------------
# Q21. Create an OAuth2PasswordBearer object for a login endpoint.
# Answer:
# from fastapi.security import OAuth2PasswordBearer
#
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="login"
# )
#
# Clarification:
# `tokenUrl="login"` informs Swagger UI where to send username & password
# when testing endpoints using the interactive authorization modal at `/docs`.

# ------------------------------------------------------------
# Q22. Create a protected /profile endpoint that extracts the bearer token.
# Answer:
# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer
#
# app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
# @app.get("/profile")
# def profile(
#     token: str = Depends(oauth2_scheme)
# ):
#     return {
#         "token": token
#     }
#
# Clarification:
# If the client omits the `Authorization: Bearer <token>` header, FastAPI automatically
# rejects the request with an HTTP 401 Unauthorized error before reaching your function body.

# ------------------------------------------------------------
# Q23. Create a get_current_user dependency.
# Answer:
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# import jwt
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# SECRET_KEY = "my_secret_key"
# ALGORITHM = "HS256"
#
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except jwt.PyJWTError:
#         raise credentials_exception
#
#     # In production: query database, e.g. db.query(User).filter_by(username=username).first()
#     user = {"username": username, "role": payload.get("role", "user")}
#     return user
#
# Clarification:
# `PyJWT` (or `python-jose`) decodes the token and validates the signature + expiration.
# The `WWW-Authenticate: Bearer` response header conforms to RFC 6750 standards.

# ------------------------------------------------------------
# Q24. Protect a /profile endpoint using get_current_user.
# Answer:
# from fastapi import Depends, FastAPI
#
# app = FastAPI()
#
# @app.get("/profile")
# def profile(
#     current_user: dict = Depends(get_current_user)
# ):
#     return current_user
#
# Clarification:
# By passing `get_current_user` into `Depends()`, FastAPI executes the entire token decoding
# and verification sequence, injecting the authenticated user object directly into `profile`.

# ------------------------------------------------------------
# Q25. Create a simple admin role check.
# Answer:
# from fastapi import HTTPException, status
#
# def require_admin(user: dict):
#     if user.get("role") != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin access required"
#         )
#
# Clarification:
# This can be used inside a route or chained as a reusable sub-dependency:
# `def get_admin_user(user: dict = Depends(get_current_user)): require_admin(user); return user`

# ------------------------------------------------------------
# Q26. Load a SECRET_KEY from an environment variable.
# Answer:
# import os
#
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback_default_for_local_dev_only")
#
# Clarification:
# In production, avoid fallback defaults for sensitive keys—raise an exception if `SECRET_KEY` is missing:
# `SECRET_KEY = os.environ["SECRET_KEY"]` (or use `pydantic_settings.BaseSettings`).

# ------------------------------------------------------------
# Q27. Create a basic login flow.
# Requirements:
# 1. Receive email and password.
# 2. Find the user.
# 3. Verify the password hash.
# 4. Generate an access token.
# 5. Return the token.
# Answer flow:
# User
#  ↓
# POST /login
#  ↓
# Find user
#  ↓
# Verify password hash
#  ↓
# Generate JWT
#  ↓
# Return access token
#
# Clarification:
# Use `OAuth2PasswordRequestForm = Depends()` or a Pydantic model for input.
# Always use constant-time string comparison (handled automatically by bcrypt/passlib) to prevent timing attacks.

# ------------------------------------------------------------
# Q28. Create the Authorization header for a bearer token.
# Answer:
# Authorization: Bearer <access_token>
#
# Clarification:
# In client code (e.g., Python `requests`, `httpx`, or JavaScript `fetch`):
# `headers = {"Authorization": f"Bearer {token}"}`

# ------------------------------------------------------------
# Q29. Create a protected endpoint that returns the
# authenticated user's information.
# Answer:
# @app.get("/profile")
# def profile(
#     current_user = Depends(get_current_user)
# ):
#     return current_user

# ------------------------------------------------------------
# Q30. Return HTTP 403 when a non-admin accesses an admin-only operation.
# Answer:
# from fastapi import HTTPException, status
#
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, current_user = Depends(get_current_user)):
#     if current_user.get("role") != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin access required"
#         )
#     return {"message": f"User {user_id} deleted successfully"}

# ============================================================
# JWT PRACTICE
# ============================================================

# ------------------------------------------------------------
# Q31. Write the conceptual structure of a JWT.
# Answer:
# HEADER.PAYLOAD.SIGNATURE
#
# Clarification:
# - Header: Algorithm and token type
# - Payload: Claims (data)
# - Signature: Cryptographic proof that header + payload have not been tampered with

# ------------------------------------------------------------
# Q32. Create an example JWT payload containing a user ID,
# role, issued-at time, and expiration time.
# Answer:
# payload = {
#     "sub": "123",
#     "role": "user",
#     "iat": 1234567890,
#     "exp": 1234569999
# }
#
# Clarification:
# Standard RFC 7519 registered claims:
# - `sub` (subject): unique identifier for the user
# - `iat` (issued at): Unix timestamp
# - `exp` (expiration): Unix timestamp after which token is invalid

# ------------------------------------------------------------
# Q33. Which information should NOT be stored in a JWT payload?
# Answer:
# Passwords
# Credit card information
# Private secrets
#
# Clarification:
# Since JWT payloads can be decoded by anyone using base64 decoding (e.g., jwt.io),
# never store plaintext secrets, credentials, or Personally Identifiable Information (PII).

# ============================================================
# MINI PROJECT
# ============================================================

# Q34. Build a basic FastAPI authentication system.
# Requirements:
# 1. Create a User model.
# 2. Store a password hash instead of a plain password.
# 3. Create POST /login.
# 4. Verify the user's password.
# 5. Generate an access token.
# 6. Create OAuth2PasswordBearer.
# 7. Create get_current_user().
# 8. Create protected GET /profile.
# 9. Add an admin-only endpoint.
# 10. Return 401 for invalid authentication.
# 11. Return 403 for insufficient permissions.
#
# Complete Runnable Implementation Example:
#
# from datetime import datetime, timedelta, timezone
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel
# import bcrypt
# import jwt
#
# app = FastAPI(title="Auth System Demo")
#
# SECRET_KEY = "super_secret_development_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
# # Mock Database
# fake_users_db = {
#     "alice": {
#         "username": "alice",
#         "hashed_password": bcrypt.hashpw(b"secret123", bcrypt.gensalt()).decode("utf-8"),
#         "role": "user"
#     },
#     "bob": {
#         "username": "bob",
#         "hashed_password": bcrypt.hashpw(b"adminpass", bcrypt.gensalt()).decode("utf-8"),
#         "role": "admin"
#     }
# }
#
# def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None or username not in fake_users_db:
#             raise credentials_exception
#         return fake_users_db[username]
#     except jwt.PyJWTError:
#         raise credentials_exception
#
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = fake_users_db.get(form_data.username)
#     if not user or not bcrypt.checkpw(form_data.password.encode("utf-8"), user["hashed_password"].encode("utf-8")):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(
#         data={"sub": user["username"], "role": user["role"]},
#         expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
#
# @app.get("/profile")
# def read_profile(current_user: dict = Depends(get_current_user)):
#     return {"username": current_user["username"], "role": current_user["role"]}
#
# @app.get("/admin/dashboard")
# def admin_dashboard(current_user: dict = Depends(get_current_user)):
#     if current_user.get("role") != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin permissions required"
#         )
#     return {"status": "Welcome to the Admin Command Center"}

# ============================================================
# AI APPLICATION PRACTICE
# ============================================================

# Q35. Design authentication for an AI Course Support API.
# Requirements:
# - Users must log in.
# - Users receive an access token.
# - /profile should be protected.
# - /recommend should identify the current user.
# - User-specific recommendations should use the authenticated user's data.
# Answer:
# User
#  ↓
# Login
#  ↓
# JWT
#  ↓
# FastAPI
#  ↓
# Authentication
#  ↓
# Current User
#  ↓
# Recommendation Service
#  ↓
# PostgreSQL
#  ↓
# User Data
#  ↓
# LLM
#  ↓
# Recommendation
#
# Clarification:
# Authenticating the user before calling the LLM allows your service to fetch personalized
# user context (past quiz history, skill gaps) and attach it to system prompts safely.

# Q36. Design authentication boundaries for an agentic AI system.
# Answer:
# User
#  ↓
# Authentication
#  ↓
# FastAPI
#  ↓
# Agent
# ├── LLM
# ├── Tools
# ├── Memory
# ├── RAG
# └── Database
# The agent should only access data and resources that belong
# to the authenticated user or that the user has permission to access.
#
# Clarification:
# Critical Security Concept: Multi-Tenant Data Isolation.
# When an agent executes a RAG search or database query tool, it MUST pass the authenticated
# `user_id` as a strict query filter (e.g., `vector_store.search(query, filter={"user_id": current_user.id})`).
# Failing to enforce boundaries at the tool layer allows prompt injection attacks to leak other users' private data.

# ============================================================
# IMPORTANT CONCEPTS TO REMEMBER
# ============================================================
# Authentication         → Who are you?
# Authorization          → What are you allowed to do?
# 401                    → Authentication missing or invalid
# 403                    → Authenticated but not allowed
# Password               → Store a secure password hash (bcrypt / argon2)
# JWT                    → Header + Payload + Signature
# Bearer Token           → Authorization: Bearer <token>
# OAuth2PasswordBearer   → Extracts bearer token from Authorization header
# Depends()              → Reusable dependency injection
# Secrets                → Environment variables / secure secret storage
# Protected Route        → Requires valid authentication
# Role-Based Authorization → Checks permissions based on user role