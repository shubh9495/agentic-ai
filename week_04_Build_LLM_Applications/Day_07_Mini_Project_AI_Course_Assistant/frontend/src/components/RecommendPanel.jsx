import { useState } from "react";
import { recommendCourse } from "../api";

export default function RecommendPanel() {
  const [goal, setGoal] = useState("Backend development");
  const [level, setLevel] = useState("Beginner");
  const [technology, setTechnology] = useState("Python");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    setAnswer("");
    setLoading(true);
    try {
      const data = await recommendCourse(goal, level, technology);
      setAnswer(data.answer);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h2>Course recommendation</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          placeholder="Your goal"
          required
        />
        <select value={level} onChange={(e) => setLevel(e.target.value)}>
          <option>Beginner</option>
          <option>Intermediate</option>
          <option>Advanced</option>
        </select>
        <input
          value={technology}
          onChange={(e) => setTechnology(e.target.value)}
          placeholder="Technology (e.g. Python)"
          required
        />
        <button disabled={loading}>
          {loading ? "Thinking..." : "Recommend"}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {answer && <div className="answer">{answer}</div>}
    </div>
  );
}