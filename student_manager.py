students = []


def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student_age= input("Enter student age: ")
    student_Course= input("Enter student course: ")
    student_versity= input("Enter student versity: ")
    students.append({"name": name, "id": student_id, "age": student_age, "course": student_Course, "versity": student_versity})
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return
    print("\nStudent List:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} (ID: {student['id']}, Age: {student['age']}, Course: {student['course']}, versity: {student['versity']})")


def update_student():
    if not students:
        print("No students to update.")
        return
    view_students()
    index = input("Enter the number of the student to update: ")
    if not index.isdigit() or int(index) < 1 or int(index) > len(students):
        print("Invalid selection.")
        return
    index = int(index) - 1
    name = input("Enter new name: ")
    student_id = input("Enter new ID: ")
    student_age = input("Enter new age: ")
    student_Course = input("Enter new course: ")
    student_versity = input("Enter new versity: ")
    students[index] = {"name": name, "id": student_id, "age": student_age, "course": student_Course, "varsity": student_versity}
    print("Student updated successfully.")


def delete_student():
    if not students:
        print("No students to delete.")
        return
    view_students()
    index = input("Enter the number of the student to delete: ")
    if not index.isdigit() or int(index) < 1 or int(index) > len(students):
        print("Invalid selection.")
        return
    index = int(index) - 1
    students.pop(index)
    print("Student deleted successfully.")


def search_student():
    query = input("Enter student name or ID to search: ")
    found = [s for s in students if query.lower() in s['name'].lower() or query == s['id']]
    if not found:
        print("No matching students found.")
        return
    print("\nSearch Results:")
    for student in found:
        print(f"{student['name']} (ID: {student['id']}, Age: {student['age']}, Course: {student['course']}, versity: {student['versity']})")


while True:
      
    print("==========================")  
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")  
    print("6. Exit")
    print("===========================")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student()
    elif choice == '6':
        print("Thank you for choosing us. Have a good day.")
        break
    else:
        print("Invalid choice. Please try again.")