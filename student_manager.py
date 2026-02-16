# Creating a simple student manager project.

students = []
# Core Functions
def add_student():
    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def view_students():
    if not students:
        print("No students found.\n")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} | Average: {student['average']:.2f} | Grade: {student['grade']}")
    print()


def search_student():
    name = input("Enter student name to search: ").lower()

    found = False
    for student in students:
        if student["name"].lower() == name:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}\n")
            found = True

    if not found:
        print("Student not found.\n")

# Main Menu
def menu():
    while True:
        print("====== Student Grade Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


menu()
