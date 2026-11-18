
from nodes import NodeManager


def seed_database(driver):
    manager = NodeManager(driver)

    students = [
        ("S001", "Aidan", "aidan@example.com", "Computer Science"),
        ("S002", "Maria", "maria@example.com", "Artificial Intelligence"),
        ("S003", "Carlos", "carlos@example.com", "Business"),
        ("S004", "Lucia", "lucia@example.com", "Mathematics"),
        ("S005", "Daniel", "daniel@example.com", "Computer Science"),
    ]

    courses = [
        ("C001", "Database Design", 3),
        ("C002", "Computer Architecture", 3),
        ("C003", "Statistics", 3),
    ]

    instructors = [
        ("I001", "Dr. Smith", "Computer Science"),
        ("I002", "Dr. Johnson", "Mathematics"),
    ]

    for student in students:
        manager.create_student(*student)
        print(f"Student added: {student[1]}")

    for course in courses:
        manager.create_course(*course)
        print(f"Course added: {course[1]}")

    for instructor in instructors:
        manager.create_instructor(*instructor)
        print(f"Instructor added: {instructor[1]}")

    print("\nDatabase seeding completed!")
