# ============================================================
# Week 05 — Day 02: Tool Schemas & Parameter Design
# Practice File
# Instructions:
# - Read each question first.
# - Uncomment the code to practice.
# - Try solving the task yourself before checking the solution.
# - The examples use Python dictionaries to represent conceptual tool schemas.
# - No provider-specific SDK is required for these exercises.
# ============================================================

# ============================================================
# Q1. Create a Basic Tool Schema
# ============================================================
# Create a schema for a tool named "get_course".
# The tool should:
# - Get course details.
# - Accept course_id.
# - course_id should be an integer.
# - course_id should be required.
#
# Expected structure:
# {
#     "name": "get_course",
#     "description": "...",
#     "parameters": {
#         ...
#     }
# }
#
# Solution:
# tool_schema = {
#     "name": "get_course",
#     "description": "Get course details by course ID.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "course_id": {
#                 "type": "integer",
#                 "description": "Unique ID of the course."
#             }
#         },
#         "required": ["course_id"]
#     }
# }
# print(tool_schema)

# ============================================================
# Q2. Create a Tool with Multiple Parameters
# ============================================================
# Create a "search_courses" schema with:
# - technology → string
# - level → string
# - max_duration → integer
#
# Solution:
# search_courses_schema = {
#     "name": "search_courses",
#     "description": "Search courses based on technology, learner level, and maximum duration.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string",
#                 "description": "Technology the learner wants to study."
#             },
#             "level": {
#                 "type": "string",
#                 "description": "Learner's current experience level."
#             },
#             "max_duration": {
#                 "type": "integer",
#                 "description": "Maximum course duration in hours."
#             }
#         },
#         "required": ["technology"]
#     }
# }
# print(search_courses_schema)

# ============================================================
# Q3. Identify Parameter Types
# ============================================================
# Decide the correct type for each:
# 1. course_name
# 2. course_id
# 3. price
# 4. is_active
# 5. topics
# 6. filters
#
# Answer:
# course_name = "string"
# course_id = "integer"
# price = "number"
# is_active = "boolean"
# topics = "array"
# filters = "object"
# print(course_name)
# print(course_id)
# print(price)
# print(is_active)
# print(topics)
# print(filters)

# ============================================================
# Q4. Required Parameter
# ============================================================
# Create a schema where course_id is required.
#
# Solution:
# schema = {
#     "name": "get_course",
#     "description": "Get course details using the course ID.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "course_id": {
#                 "type": "integer"
#             }
#         },
#         "required": ["course_id"]
#     }
# }
# print(schema)

# ============================================================
# Q5. Required and Optional Parameters
# ============================================================
# Create a search_courses schema where:
# - technology → required
# - level → optional
# - max_duration → optional
#
# Solution:
# schema = {
#     "name": "search_courses",
#     "description": "Search available courses.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string"
#             },
#             "level": {
#                 "type": "string"
#             },
#             "max_duration": {
#                 "type": "integer"
#             }
#         },
#         "required": ["technology"]
#     }
# }
# print(schema)

# ============================================================
# Q6. Add Parameter Descriptions
# ============================================================
# Improve this parameter:
# {
#     "course_id": {
#         "type": "integer"
#     }
# }
# Add a useful description.
#
# Solution:
# course_id = {
#     "type": "integer",
#     "description": "Unique ID of the course."
# }
# print(course_id)

# ============================================================
# Q7. Create an Enum Parameter
# ============================================================
# Create a level parameter that accepts only:
# - beginner
# - intermediate
# - advanced
#
# Solution:
# level = {
#     "type": "string",
#     "enum": [
#         "beginner",
#         "intermediate",
#         "advanced"
#     ],
#     "description": "Learner's current experience level."
# }
# print(level)

# ============================================================
# Q8. Create a Boolean Parameter
# ============================================================
# Create an include_inactive boolean parameter.
#
# Solution:
# include_inactive = {
#     "type": "boolean",
#     "description": "Whether inactive courses should also be included."
# }
# print(include_inactive)

# ============================================================
# Q9. Create an Array Parameter
# ============================================================
# Create a topics parameter that accepts multiple topics.
#
# Solution:
# topics = {
#     "type": "array",
#     "description": "List of topics related to the course."
# }
# print(topics)

# ============================================================
# Q10. Create an Object Parameter
# ============================================================
# Create a user_preferences object containing:
# - level
# - technology
# - goal
#
# Solution:
# user_preferences = {
#     "type": "object",
#     "properties": {
#         "level": {
#             "type": "string"
#         },
#         "technology": {
#             "type": "string"
#         },
#         "goal": {
#             "type": "string"
#         }
#     }
# }
# print(user_preferences)

# ============================================================
# Q11. Add a Default Value
# ============================================================
# Create a level parameter with:
# - type = string
# - default = beginner
#
# Solution:
# level = {
#     "type": "string",
#     "default": "beginner",
#     "description": "Learner's experience level."
# }
# print(level)

# ============================================================
# Q12. Create a Nested Parameter
# ============================================================
# Create a filters object containing:
# - technology
# - level
# - duration
#
# Solution:
# filters = {
#     "type": "object",
#     "properties": {
#         "technology": {
#             "type": "string"
#         },
#         "level": {
#             "type": "string"
#         },
#         "duration": {
#             "type": "integer"
#         }
#     }
# }
# print(filters)

# ============================================================
# Q13. Complete search_courses Schema
# ============================================================
# Create the complete schema:
# Name:
# search_courses
# Required:
# technology
# Optional:
# level
# max_duration
# level should use an enum:
# beginner
# intermediate
# advanced
#
# Solution:
# search_courses_schema = {
#     "name": "search_courses",
#     "description": (
#         "Search courses based on technology, learner level, "
#         "and maximum duration."
#     ),
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string",
#                 "description": "Technology the learner wants to study."
#             },
#             "level": {
#                 "type": "string",
#                 "enum": [
#                     "beginner",
#                     "intermediate",
#                     "advanced"
#                 ],
#                 "description": "Learner's current experience level."
#             },
#             "max_duration": {
#                 "type": "integer",
#                 "description": "Maximum course duration in hours."
#             }
#         },
#         "required": ["technology"]
#     }
# }
# print(search_courses_schema)

# ============================================================
# Q14. Match Python Function and Schema
# ============================================================
# Python function:
# def search_courses(
#     technology: str,
#     level: str | None = None,
#     max_duration: int | None = None
# ):
#     ...
# Create a schema that matches this function.
#
# Solution:
# def search_courses(
#     technology: str,
#     level: str | None = None,
#     max_duration: int | None = None
# ):
#     return {
#         "technology": technology,
#         "level": level,
#         "max_duration": max_duration
#     }
#
# search_courses_schema = {
#     "name": "search_courses",
#     "description": "Search available courses.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string"
#             },
#             "level": {
#                 "type": "string"
#             },
#             "max_duration": {
#                 "type": "integer"
#             }
#         },
#         "required": ["technology"]
#     }
# }
# print(search_courses_schema)

# ============================================================
# Q15. Validate Required Parameters
# ============================================================
# Write a simple validation function that checks whether
# technology exists in the tool arguments.
# Example:
# valid:
# {"technology": "Python"}
# invalid:
# {}
#
# Solution:
# def validate_search_arguments(arguments):
#     if "technology" not in arguments:
#         return False
#     return True
#
# print(validate_search_arguments({"technology": "Python"}))
# print(validate_search_arguments({}))

# ============================================================
# Q16. Validate Parameter Type
# ============================================================
# Write a function that validates course_id.
# course_id must be an integer.
#
# Solution:
# def validate_course_id(arguments):
#     course_id = arguments.get("course_id")
#     if not isinstance(course_id, int):
#         return False
#     return True
#
# print(validate_course_id({"course_id": 10}))
# print(validate_course_id({"course_id": "10"}))

# ============================================================
# Q17. Validate Enum Value
# ============================================================
# Validate that level is one of:
# beginner
# intermediate
# advanced
#
# Solution:
# def validate_level(level):
#     allowed_levels = {
#         "beginner",
#         "intermediate",
#         "advanced"
#     }
#     return level in allowed_levels
#
# print(validate_level("beginner"))
# print(validate_level("expert"))

# ============================================================
# Q18. Build a General Tool Validator
# ============================================================
# Create a validator that checks:
# - technology is present
# - level is valid if provided
# - max_duration is an integer if provided
#
# Solution:
# def validate_search_courses(arguments):
#     if "technology" not in arguments:
#         return False
#     allowed_levels = {
#         "beginner",
#         "intermediate",
#         "advanced"
#     }
#     level = arguments.get("level")
#     if level is not None and level not in allowed_levels:
#         return False
#     max_duration = arguments.get("max_duration")
#     if max_duration is not None and not isinstance(max_duration, int):
#         return False
#     return True
#
# print(
#     validate_search_courses(
#         {
#             "technology": "Python",
#             "level": "beginner",
#             "max_duration": 30
#         }
#     )
# )
# print(
#     validate_search_courses(
#         {
#             "technology": "Python",
#             "level": "expert"
#         }
#     )
# )

# ============================================================
# Q19. Identify a Bad Schema
# ============================================================
# What is wrong with this schema?
# bad_schema = {
#     "name": "search",
#     "description": "Search stuff.",
#     "parameters": {
#         "data": {
#             "type": "string"
#         }
#     }
# }
# Think about:
# - Tool name
# - Description
# - Parameter structure
# - Required fields
#
# Answer:
# Problems:
# 1. "search" is too vague.
# 2. "Search stuff." does not explain the tool.
# 3. "data" is vague.
# 4. The parameter structure does not clearly describe the expected contract.
# 5. Required fields are not clearly defined.

# ============================================================
# Q20. Improve a Bad Tool Schema
# ============================================================
# Convert the following into a better schema:
# Name:
# search
# Description:
# Search stuff.
# Parameter:
# data
#
# Solution:
# good_schema = {
#     "name": "search_courses",
#     "description": (
#         "Search available courses based on technology, "
#         "learner level, and maximum duration."
#     ),
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string",
#                 "description": "Technology the learner wants to study."
#             },
#             "level": {
#                 "type": "string",
#                 "enum": [
#                     "beginner",
#                     "intermediate",
#                     "advanced"
#                 ],
#                 "description": "Learner's current experience level."
#             },
#             "max_duration": {
#                 "type": "integer",
#                 "description": "Maximum course duration in hours."
#             }
#         },
#         "required": ["technology"]
#     }
# }
# print(good_schema)

# ============================================================
# Q21. Choose the Correct Tool
# ============================================================
# Available tools:
# 1. search_courses
# → Find courses matching user requirements.
# 2. get_course
# → Get details of a specific course.
# 3. get_course_price
# → Get the price of a specific course.
#
# User:
# "Find beginner Python courses."
# Which tool should be selected?
#
# Answer:
# selected_tool = "search_courses"
# print(selected_tool)

# ============================================================
# Q22. Choose Another Tool
# ============================================================
# User:
# "How much does course 10 cost?"
# Which tool should be selected?
#
# Answer:
# selected_tool = "get_course_price"
# print(selected_tool)

# ============================================================
# Q23. Create a Course Price Tool Schema
# ============================================================
# Create a schema for:
# get_course_price(course_id)
# course_id:
# - integer
# - required
#
# Solution:
# schema = {
#     "name": "get_course_price",
#     "description": "Get the price of a specific course using its course ID.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "course_id": {
#                 "type": "integer",
#                 "description": "Unique ID of the course."
#             }
#         },
#         "required": ["course_id"]
#     }
# }
# print(schema)

# ============================================================
# Q24. Create a Weather Tool Schema
# ============================================================
# Create a weather tool:
# get_weather(city)
# city:
# - string
# - required
#
# Solution:
# weather_schema = {
#     "name": "get_weather",
#     "description": "Get weather information for a city.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "city": {
#                 "type": "string",
#                 "description": "Name of the city."
#             }
#         },
#         "required": ["city"]
#     }
# }
# print(weather_schema)

# ============================================================
# Q25. Create a Support Ticket Tool Schema
# ============================================================
# Create:
# create_support_ticket(
#     title,
#     description,
#     priority
# )
# Rules:
# title → string → required
# description → string → required
# priority → enum → optional
# Allowed priority values:
# low
# medium
# high
#
# Solution:
# support_ticket_schema = {
#     "name": "create_support_ticket",
#     "description": "Create a support ticket for a user issue.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "title": {
#                 "type": "string",
#                 "description": "Short title describing the issue."
#             },
#             "description": {
#                 "type": "string",
#                 "description": "Detailed description of the issue."
#             },
#             "priority": {
#                 "type": "string",
#                 "enum": [
#                     "low",
#                     "medium",
#                     "high"
#                 ],
#                 "description": "Priority of the support issue."
#             }
#         },
#         "required": ["title", "description"]
#     }
# }
# print(support_ticket_schema)

# ============================================================
# Q26. Tool Schema and Validation Flow
# ============================================================
# Write the complete conceptual flow.
# Expected:
# Tool Schema
# ↓
# LLM
# ↓
# Tool Arguments
# ↓
# Backend Validation
# ↓
# Execute Tool
#
# Answer:
# flow = [
#     "Tool Schema",
#     "LLM",
#     "Tool Arguments",
#     "Backend Validation",
#     "Execute Tool"
# ]
# for step in flow:
#     print(step)

# ============================================================
# Q27. Mini Project — Course Search Tool
# ============================================================
# Build a complete conceptual tool definition for:
# search_courses
# Requirements:
# - technology → required string
# - level → optional enum
# - max_duration → optional integer
# Then create a simple Python function that accepts these
# arguments.
#
# Solution:
# search_courses_schema = {
#     "name": "search_courses",
#     "description": (
#         "Search available courses based on technology, "
#         "learner level, and maximum duration."
#     ),
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "technology": {
#                 "type": "string",
#                 "description": "Technology the learner wants to study."
#             },
#             "level": {
#                 "type": "string",
#                 "enum": [
#                     "beginner",
#                     "intermediate",
#                     "advanced"
#                 ],
#                 "description": "Learner's current experience level."
#             },
#             "max_duration": {
#                 "type": "integer",
#                 "description": "Maximum course duration in hours."
#             }
#         },
#         "required": ["technology"]
#     }
# }
#
# def search_courses(
#     technology: str,
#     level: str | None = None,
#     max_duration: int | None = None
# ):
#     return {
#         "technology": technology,
#         "level": level,
#         "max_duration": max_duration
#     }
#
# arguments = {
#     "technology": "Python",
#     "level": "beginner",
#     "max_duration": 30
# }
# print(search_courses(**arguments))

# ============================================================
# Q28. Interview Practice
# ============================================================
# Answer these questions yourself:
# 1. What is a tool schema?
# 2. Why are tool schemas important?
# 3. What is the difference between required and optional parameters?
# 4. What is an enum?
# 5. Why are parameter descriptions useful?
# 6. Does a schema replace backend validation?
# 7. What makes a good tool schema?
# 8. Why should tool parameters be minimal?
#
# Answers:
# 1. A tool schema is a structured description of a tool,
#    including its name, purpose, parameters, types, and
#    required inputs.
# 2. It helps the LLM understand available tools and generate
#    appropriate arguments.
# 3. A required parameter must be provided, while an optional
#    parameter can be omitted.
# 4. An enum restricts a parameter to predefined values.
# 5. They give the LLM more context and reduce ambiguity.
# 6. No. Backend validation is still required.
# 7. Clear name, useful description, correct types, clear
#    descriptions, appropriate required fields, restricted
#    values where needed, and minimal parameters.
# 8. Tools should request only the information they actually
#    need.

# ============================================================
# Q29. Final Revision
# ============================================================
# Complete the mental model:
# Tool Schema
# ↓
# ______________________
# ↓
# ______________________
# ↓
# Backend Validation
# ↓
# ______________________
# ↓
# Tool Result
#
# Answer:
# Tool Schema
# ↓
# Understand Available Tools
# ↓
# Choose Tool
# ↓
# Backend Validation
# ↓
# Execute Tool
# ↓
# Tool Result

# ============================================================
# FINAL MINI PROJECT
# ============================================================
# Build a conceptual Tool-Enabled Course Assistant.
# It should have these tools:
# 1. search_courses
# 2. get_course
# 3. get_course_price
#
# For each tool:
# - Create a clear name.
# - Write a useful description.
# - Define parameters.
# - Use correct parameter types.
# - Mark required parameters.
# - Use enums where appropriate.
# - Add parameter descriptions.
#
# Then create a simple tool registry:
# tool_registry = {
#     "search_courses": search_courses_schema,
#     "get_course": get_course_schema,
#     "get_course_price": get_course_price_schema
# }
#
# Finally, explain the flow:
# User
# ↓
# LLM
# ↓
# Understand Available Tools
# ↓
# Choose Tool
# ↓
# Generate Arguments
# ↓
# Backend Validation
# ↓
# Execute Tool
# ↓
# Tool Result
# ↓
# LLM
# ↓
# Final Response