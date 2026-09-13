# Writing a program that takes information from 4 students and saves it in a file

students = []
for i in range(4):
    print(f"\n enter student information {i +1}")
    name = input("please enter your name: " )
    age = int(input("please enter your age: "))
    student_id_number = int(input(" please enter your student ID: "))
    student = {
        "name" : name , 
        "age" : age ,
        "student ID" : student_id_number
    }
    students.append(student)

# saving students informations ina file
students = open("students.txt", "w")
students.write("Student Information:\n")


# Read students from the file
print("\nStudents saved in the file:")

students = open("students.txt", "r")
students_content = students.read()
print(students_content)

students = open ("students.txt", "r").close()
print("students.txt file has been closed.")
students = open("students.txt", "w").close()
print("students.txt file has been cleared.")