from database import create_database, add_student, show_students

create_database()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. List Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))

        add_student(name, age)

        print("Student Added!")

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")