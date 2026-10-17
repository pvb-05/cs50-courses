CREATE INDEX "a"
ON "enrollments"("course_id");

CREATE INDEX "b"
ON "enrollments"("student_id");

CREATE INDEX "c"
ON "courses"("department", "semester", "number");

CREATE INDEX "e"
ON "courses"("semester", "title");

CREATE INDEX "f"
ON courses(semester);

CREATE INDEX "g"
ON "satisfies"("course_id", "requirement_id");
