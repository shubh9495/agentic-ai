import { useState } from "react";
import { askQuestionStream } from "../api";

export default function AskPanel({ courseId }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    if (!courseId) {
      setError("Please select a course first.");
      return;
    }

    setError("");
    setAnswer("");
    setLoading(true);

    try {
      await askQuestionStream(courseId, question, (chunk) =>
        setAnswer((prev) => prev + chunk)
      );
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h2>Ask about the selected course</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="What will I learn in this course?"
          minLength={3}
          required
        />
        <button disabled={loading}>{loading ? "Answering..." : "Ask"}</button>
      </form>
      {error && <p className="error">{error}</p>}
      {answer && <div className="answer">{answer}</div>}
    </div>
  );
}