from typing import AsyncIterator

from google import genai

from app.config import LLM_API_KEY, LLM_MODEL
from app.prompts.course_prompts import SYSTEM_PROMPT


client = genai.Client(api_key=LLM_API_KEY)

MAX_TOKENS = 800


class LLMServiceError(Exception):
    """Application-level LLM error. Safe to show to the client."""

    def __init__(self, message: str, status_code: int = 502):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def _translate_error(exc: Exception) -> LLMServiceError:
    error_message = str(exc).lower()

    if "429" in error_message or "rate" in error_message:
        return LLMServiceError(
            "The AI service is busy. Please try again shortly.",
            429,
        )

    if "timeout" in error_message:
        return LLMServiceError(
            "The AI service timed out. Please try again.",
            504,
        )

    if "connection" in error_message:
        return LLMServiceError(
            "Could not reach the AI service.",
            502,
        )

    return LLMServiceError(
        "Unexpected AI service error.",
        500,
    )


async def ask_llm(
    prompt: str,
    system: str = SYSTEM_PROMPT,
) -> str:
    """Normal non-streaming call: waits for the full answer."""

    try:
        response = await client.aio.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config={
                "system_instruction": system,
                "max_output_tokens": MAX_TOKENS,
            },
        )

        return response.text

    except Exception as exc:
        raise _translate_error(exc) from exc


async def stream_llm(
    prompt: str,
    system: str = SYSTEM_PROMPT,
) -> AsyncIterator[str]:
    """Streaming call: yields text chunks as they arrive."""

    try:
        response = await client.aio.models.generate_content_stream(
            model=LLM_MODEL,
            contents=prompt,
            config={
                "system_instruction": system,
                "max_output_tokens": MAX_TOKENS,
            },
        )

        async for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as exc:
        err = _translate_error(exc)
        yield f"\n\n[Error: {err.message}]"