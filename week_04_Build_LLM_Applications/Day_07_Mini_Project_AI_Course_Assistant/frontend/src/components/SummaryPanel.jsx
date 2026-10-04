import { useState } from "react";
import { summarizeCourse } from "../api";

export default function SummaryPanel({ courseId }) {
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleClick() {
    if (!courseId) {
      setError("Please select a course first.");
      return;
    }
    setError("");
    setAnswer("");
    setLoading(true);
    try {
      const data = await summarizeCourse(courseId);
      setAnswer(data.answer);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h2>Course summary</h2>
      <button onClick={handleClick} disabled={loading}>
        {loading ? "Summarizing..." : "Summarize selected course"}
      </button>
      {error && <p className="error">{error}</p>}
      {answer && <div className="answer">{answer}</div>}
    </div>
  );
}