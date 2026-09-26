# Day 01: HTTP & REST API Fundamentals
# ============================================================
# INTERVIEW QUESTIONS
# ============================================================
# 1. What is an API?
# Answer:
# An API is a defined interface that allows one software system
# to communicate with another.
# 2. What is HTTP?
# Answer:
# HTTP is a communication protocol used to exchange requests
# and responses between clients and servers.
# 3. What is the difference between a client and a server?
# Answer:
# A client sends requests.
# A server receives requests, processes them, and returns responses.
# 4. What is an HTTP request?
# Answer:
# An HTTP request is a message sent by a client to a server.
# It can contain a method, URL, headers, query parameters,
# path parameters, and a body.
# 5. What is an HTTP response?
# Answer:
# An HTTP response is the message returned by the server.
# It commonly contains a status code, headers, and a body.
# 6. What is REST?
# Answer:
# REST is an architectural style for designing networked
# applications around resources, URLs, HTTP methods, status
# codes, and stateless requests.
# REST architectural constraints/principles/rules
# 7. Client-Server
# 8. Stateless
# 9. Uniform Interface
# 10. Resource-Based
# 11. Cacheable
# 12. Layered System
# 13. What is a REST API?
# Answer:
# A REST API is an API designed using REST principles,
# commonly using HTTP methods and resource-based URLs.
# REST = A set of rules for designing an API
# REST API = An API that follows REST principles
# Endpoint = A specific URL of an API
# 14. What is a resource?
# Answer:
# A resource is an entity that an API manages or exposes.
# Examples:
# /users
# /courses
# /products
# /orders
# 15. What is an endpoint?
# Answer:
# An endpoint is a specific combination of an HTTP method and URL
# through which a client interacts with an API.
# Example:
# GET /courses
# 16. Why are REST APIs commonly used?
# Answer:
# REST APIs provide a simple and standard way for different
# applications to communicate over HTTP using resources,
# HTTP methods, and status codes.
# 17. What are HTTP Methods in REST API?
# Answer:
# HTTP methods define what action we want to perform on a resource.
#
# GET    → Used to retrieve data.
# POST   → Used to create a resource or submit data for processing.
# PUT    → Used to replace or update an existing resource.
# PATCH  → Used to partially update an existing resource.
# DELETE → Used to delete a resource.
#
# PUT vs PATCH:
# PUT generally replaces the entire resource.
# PATCH updates only the specified fields.
# 18. What is a query parameter?
# Answer:
# A query parameter is an optional value added to the URL after ?.
# Example:
# /courses?level=beginner
# 19. What is a path parameter?
# Answer:
# A path parameter is a value in the URL used to identify a specific resource.
# Example:
# /courses/10
# 20. What is the difference between query and path parameters?
# Answer:
# Path parameters identify a specific resource.
# Query parameters are commonly used for filtering, searching, sorting, pagination, or optional configuration.
# 21. What is a request body?
# Answer:
# The request body contains data sent by the client to the server.
# JSON is commonly used as the request body format.
# 22. What are HTTP headers?
# Answer:
# Headers carry additional information about a request or response.
# Examples:
# Content-Type
# Authorization
# Accept
# User-Agent
# 23. What is Content-Type?
# Answer:
# Content-Type tells the receiver what format the message body uses.
# Example:
# Content-Type: application/json
# 24. What are the common HTTP status codes in REST API?
# Answer:
# HTTP status codes tell the client what happened with the request.
#
# 200 → Request was successfully processed.
# 201 → A new resource was successfully created.
# 400 → Bad Request; the request is invalid.
# 401 → Unauthorized; authentication is required or credentials are invalid.
# 403 → Forbidden; the client is authenticated but not allowed to perform
#        the operation.
# 404 → Not Found; the requested resource does not exist.
# 422 → Unprocessable Content; the request is valid but fails validation.
# 500 → Internal Server Error; an unexpected error occurred on the server.
#
# 200 vs 201:
# 200 means the request was successful.
# 201 means a new resource was successfully created.
#
# 401 vs 403:
# 401 means authentication is missing or invalid.
# 403 means the server understood the request but access is not allowed.
# 25. How would FastAPI communicate with an LLM API?
# Answer:
# FastAPI receives the client request, validates the input,
# calls the LLM provider API, processes the result, and
# returns an HTTP response to the client.
# 26. How can an agent be exposed through an API?
# Answer:
# An endpoint such as:
# POST /agent/run
# can receive a task, pass it to an agent, allow the agent
# to use tools or memory, and return the final result.
# 27. Why is FastAPI useful for Agentic AI applications?
# Answer:
# FastAPI provides type hints, request validation, automatic
# API documentation, async support, Pydantic integration,
# and dependency injection, which are useful for building
# AI backend APIs.
# ============================================================
# CODING PRACTICE
# ============================================================
# 28. CREATE AN HTTP REQUEST REPRESENTATION
# Create a Python dictionary representing:
# POST /recommend
# Headers
# Content-Type: application/json
# Body:
# {
# "goal": "Java backend developer"
# }
# Answer:
# request = {
# "method": "POST",
# "url": "/recommend",
# "headers": {
# "Content-Type": "application/json"
# },
# "body": {
# "goal": "Java backend developer"
# }
# }
# print(request)
# 29. CREATE AN HTTP RESPONSE
# Create a response representation containing:
# status code = 200
# content type = application/json
# body = {"message": "Success"}
# Answer:
# response = {
# "status_code": 200,
# "headers": {
# "Content-Type": "application/json"
# },
# "body": {
# "message": "Success"
# }
# }
# print(response)
# 30. READ QUERY PARAMETERS
# Given:
# url = "/courses?level=beginner&limit=10"
# Extract level and limit.
# Answer:
# from urllib.parse import urlparse, parse_qs
# url = "/courses?level=beginner&limit=10"
# parsed_url = urlparse(url)
# params = parse_qs(parsed_url.query)
# level = params["level"][0]
# limit = int(params["limit"][0])
# print(level)
# print(limit)
# 31. EXTRACT A PATH PARAMETER
# Given:
# url = "/courses/10"
# Extract the course ID.
# Answer:
# url = "/courses/10"
# parts = url.strip("/").split("/")
# course_id = int(parts[-1])
# print(course_id)
# 32. BUILD A REST ENDPOINT
# Create a function that returns the endpoint information
# for a course.
# Example:
# GET /courses/10
# Answer:
# def get_course_endpoint(course_id):
# return {
# "method": "GET",
# "url": f"/courses/{course_id}"
# }
# print(get_course_endpoint(10))
# 33. VALIDATE A REQUEST BODY
# Validate that a recommendation request contains:
# - goal
# - skills
# Answer:
# def validate_request(data):
# if "goal" not in data:
# return False
# if "skills" not in data:
# return False
# return True
# request = {
# "goal": "Java backend developer",
# "skills": ["Java", "SQL"]
# }
# print(validate_request(request))
# 34. RETURN DIFFERENT STATUS CODES
# Create a function that returns:
# 201 if a resource is created
# 400 if required data is missing
# Answer:
# def create_course(data):
# if "name" not in data:
# return {
# "status_code": 400,
# "message": "Course name is required"
# }
# return {
# "status_code": 201,
# "message": "Course created"
# }
# print(create_course({"name": "Spring Boot"}))
# print(create_course({}))
# 35. SIMULATE A REST API
# Create a simple function that handles:
# GET /courses
# GET /courses/{id}
# POST /courses
# DELETE /courses/{id}
# Return an appropriate response for each operation.
# Answer:
# courses = {
# 1: {"name": "Java"},
# 2: {"name": "Spring Boot"}
# }
# def api_request(method, path, body=None):
# if method == "GET" and path == "/courses":
# return {
# "status_code": 200,
# "body": list(courses.values())
# }
# if method == "POST" and path == "/courses":
# course_id = max(courses.keys(), default=0) + 1
# courses[course_id] = body
# return {
# "status_code": 201,
# "body": courses[course_id]
# }
# if method == "GET" and path.startswith("/courses/"):
# course_id = int(path.split("/")[-1])
# if course_id not in courses:
# return {
# "status_code": 404,
# "body": {"message": "Course not found"}
# }
# return {
# "status_code": 200,
# "body": courses[course_id]
# }
# if method == "DELETE" and path.startswith("/courses/"):
# course_id = int(path.split("/")[-1])
# if course_id not in courses:
# return {
# "status_code": 404,
# "body": {"message": "Course not found"}
# }
# del courses[course_id]
# return {
# "status_code": 204,
# "body": None
# }
# return {
# "status_code": 400,
# "body": {"message": "Invalid request"}
# }
# print(api_request("GET", "/courses"))
# print(api_request("GET", "/courses/1"))
# print(api_request(
# "POST",
# "/courses",
# {"name": "FastAPI"}
# ))
# print(api_request("DELETE", "/courses/1"))
# 36. AI RECOMMENDATION API FLOW
# Simulate:
# Client
# ↓
# POST /recommend
# ↓
# Validate request
# ↓
# Generate recommendation
# ↓
# Return response
# Answer:
# def recommend(data):
# if "goal" not in data:
# return {
# "status_code": 400,
# "body": {"message": "goal is required"}
# }
# recommendations = [
# {
# "course": "Spring Boot",
# "reason": "Useful for Java backend development"
# },
# {
# "course": "REST API Development",
# "reason": "Useful for backend API development"
# }
# ]
# return {
# "status_code": 200,
# "body": {
# "goal": data["goal"],
# "recommendations": recommendations
# }
# }
# request = {
# "goal": "Become a Java backend developer"
# }
# print(recommend(request))
# 37. MINI PROJECT
# Build a simple in-memory Course REST API.
# Requirements:
# GET    /courses
# GET    /courses/{id}
# POST   /courses
# PATCH  /courses/{id}
# DELETE /courses/{id}
# Requirements:
# 38. Store courses in a dictionary.
# 39. Return 200 for successful GET requests.
# 40. Return 201 when creating a course.
# 41. Return 204 after successful deletion.
# 42. Return 404 when a course does not exist.
# 43. Return 400 when request data is invalid.
# Answer:
# # Implement this yourself first.
# # Suggested structure:
# # courses = {}
# # def get_courses():
# #     pass
# # def get_course(course_id):
# #     pass
# # def create_course(data):
# #     pass
# # def update_course(course_id, data):
# #     pass
# # def delete_course(course_id):
# #     pass
# # The goal is to practice:
# # HTTP methods
# # REST resources
# # Path parameters
# # Request bodies
# # Status codes
# # API request/response flow