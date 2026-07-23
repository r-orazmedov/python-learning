import sqlite3


def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)

    connection.commit()
    connection.close()

def add_student(name, age):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students (name, age)
    VALUES (?, ?)
    """, (name, age))

    connection.commit()
    connection.close()

def show_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM students""")

    students = cursor.fetchall()

    if not students:
        print("No students found.")
        connection.close()
        return

    print("===== List of students =====")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print("-" * 30)

    connection.close()

def find_student(name):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM students 
    WHERE name = ?
    """, (name,))

    students = cursor.fetchall()

    if not students:
        print("Student not found.")
        connection.close()
        return

    for student in students:
        print(f"\nID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")

    connection.close()

def update_student(student_id, new_name, new_age):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?
    WHERE id = ?""", (new_name, new_age, student_id))

    connection.commit()
    connection.close()

def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM students
    WHERE id = ?""", (student_id,))

    connection.commit()
    connection.close()