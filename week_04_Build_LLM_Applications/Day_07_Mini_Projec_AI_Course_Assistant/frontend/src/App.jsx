import { useEffect, useState } from "react";
import { getCourses } from "./api";
import CourseList from "./components/CourseList";
import AskPanel from "./components/AskPanel";
import RecommendPanel from "./components/RecommendPanel";
import SummaryPanel from "./components/SummaryPanel";
import "./App.css";

export default function App() {
  const [courses, setCourses] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getCourses()
      .then(setCourses)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div className="container">
      <h1>AI Course Assistant</h1>
      {error && <p className="error">Could not load courses: {error}</p>}

      <div className="layout">
        <CourseList
          courses={courses}
          selectedId={selectedId}
          onSelect={setSelectedId}
        />
        <div className="panels">
          <AskPanel courseId={selectedId} />
          <SummaryPanel courseId={selectedId} />
          <RecommendPanel />
        </div>
      </div>
    </div>
  );
}