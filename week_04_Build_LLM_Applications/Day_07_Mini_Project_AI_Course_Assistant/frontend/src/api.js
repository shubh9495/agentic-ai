const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function request(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (!response.ok) {
    let message = "Something went wrong";
    try {
      const data = await response.json();
      // FastAPI returns { detail: "..." } (or a list for validation errors)
      message =
        typeof data.detail === "string"
          ? data.detail
          : "Please check your input and try again.";
    } catch {
      // ignore JSON parse errors
    }
    throw new Error(message);
  }
  return response.json();
}

export const getCourses = () => request("/courses");

export const askQuestion = (courseId, question) =>
  request("/ai/ask", {
    method: "POST",
    body: JSON.stringify({ course_id: courseId, question }),
  });

export const recommendCourse = (goal, level, technology) =>
  request("/ai/recommend", {
    method: "POST",
    body: JSON.stringify({ goal, level, technology }),
  });

export const summarizeCourse = (courseId) =>
  request("/ai/summarize", {
    method: "POST",
    body: JSON.stringify({ course_id: courseId }),
  });

/**
 * Streaming: calls onChunk(text) every time a new piece arrives.
 */
export async function askQuestionStream(courseId, question, onChunk) {
  const response = await fetch(`${BASE_URL}/ai/ask/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ course_id: courseId, question }),
  });

  if (!response.ok) {
    let message = "Something went wrong";
    try {
      const data = await response.json();
      if (typeof data.detail === "string") message = data.detail;
    } catch {
      // ignore
    }
    throw new Error(message);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    onChunk(decoder.decode(value, { stream: true }));
  }
}