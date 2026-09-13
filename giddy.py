# Writing a program that takes information from 4 students and saves it in a file

students = []
for i in range(4):
    print(f"\n enter student information {i +1}")
    name = input("please enter your name: " )
    age = int(input("please enter your age: "))
    student_id_number = int(input(" please enter your student ID: "))
    student = {
        "name": name,
        "age": age,
        "student ID": student_id_number
    }
    students.append(student)

# Saving students' information in a file
file = open("students.txt", "w")
file.write("Student Information:\n")
for student in students:
    file.write(
    f"Name: {student['name']}, "
        f"Age: {student['age']}, "
        f"Student ID: {student['student ID']}\n"
    )
file.close()

# Read students from the file
print("\nStudents saved in the file:")
file = open("students.txt", "r")
students_content = file.read()
print(students_content)
file.close()
print("students.txt file has been closed.")