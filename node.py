class NodeManager:
    def __init__(self, driver):
        self.driver = driver

    def create_student(self, student_id, name, email, major):
        query = """
        MERGE (s:Student {student_id: $student_id})
        ON CREATE SET
            s.name = $name,
            s.email = $email,
            s.major = $major
        RETURN s
        """

        with self.driver.session() as session:
            record = session.run(
                query,
                student_id=student_id,
                name=name,
                email=email,
                major=major
            ).single()

            return record["s"]

    def create_course(self, course_id, course_name, credits):
        query = """
        MERGE (c:Course {course_id: $course_id})
        ON CREATE SET
            c.course_name = $course_name,
            c.credits = $credits
        RETURN c
        """

        with self.driver.session() as session:
            record = session.run(
                query,
                course_id=course_id,
                course_name=course_name,
                credits=credits
            ).single()

            return record["c"]

    def create_instructor(
        self, instructor_id, instructor_name, department
    ):
        query = """
        MERGE (i:Instructor {instructor_id: $instructor_id})
        ON CREATE SET
            i.instructor_name = $instructor_name,
            i.department = $department
        RETURN i
        """

        with self.driver.session() as session:
            record = session.run(
                query,
                instructor_id=instructor_id,
                instructor_name=instructor_name,
                department=department
            ).single()

            return record["i"]
