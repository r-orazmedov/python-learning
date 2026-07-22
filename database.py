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

    print("===== List of students =====")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print("-" * 30)

    connection.close()