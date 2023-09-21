# School class
class School:
    def __init__(self):
        self.students = []

    # Add students
    def add_student(self):
        student = Student(name, standard, roll_number)
        self.students.append(student)

    # Display student list
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Standard: {student.standard}")
            print(f"Roll Number: {student.roll_number}")
            print("-----------------------------------")

    # Edit student details
    def edit_student(self, new_name, new_standard, edit_number):
        for student in self.students:
            if student.roll_number == edit_number:
                student.name = new_name
                student.standard = new_standard

    # Delete student details
    def delete_student(self, delete_number):
        for student in self.students:
            if student.roll_number == delete_number:
                self.students.remove(student)


# Student class
class Student:
    def __init__(self, name, standard, roll_number):
        self.name = name
        self.standard = standard
        self.roll_number = roll_number


# Create school
school = School()
# Accept input from user
while True:
    choice = input("Enter a Task:\n1.Add Student\n2.Display Student\n3.Edit Student\n"
                   "4.Delete Student\n5.Exit\n")
    if choice == "1":
        name = input("Enter student name: ")
        standard = input("Enter the standard: ")
        roll_number = input("Enter roll number: ")
        school.add_student()
    elif choice == "2":
        school.display_students()
    elif choice == "3":
        edit_number = input("Enter the roll number to Edit: ")
        new_name = input("Enter new name: ")
        new_standard = input("Enter new standard: ")
        school.edit_student(new_name, new_standard, edit_number)
    elif choice == "4":
        delete_number = input("Enter the roll number to Delete: ")
        school.delete_student(delete_number)
    elif choice == "5":
        break
