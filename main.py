from database import create_database, add_student, show_students, find_student, update_student, delete_student

create_database()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. List Students")
    print("3. Find Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))

        add_student(name, age)

        print("Student Added!")

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Name: ")

        find_student(name)

    elif choice == "4":
        student_id = int(input("Student ID: "))
        new_name = input("New Name: ")
        new_age = int(input("New Age: "))

        update_student(student_id, new_name, new_age)

        print("Student updated!")

    elif choice == "5":
        student_id = int(input("Student ID: "))

        delete_student(student_id)

        print("Student deleted!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")