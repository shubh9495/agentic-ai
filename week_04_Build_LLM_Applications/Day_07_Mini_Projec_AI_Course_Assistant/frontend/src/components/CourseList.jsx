export default function CourseList({ courses, selectedId, onSelect }) {
  return (
    <div className="card">
      <h2>Courses</h2>
      <ul className="course-list">
        {courses.map((course) => (
          <li
            key={course.id}
            className={course.id === selectedId ? "course selected" : "course"}
            onClick={() => onSelect(course.id)}
          >
            <strong>{course.name}</strong>
            <span>
              {course.level} · {course.technology} · {course.duration}h
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}