# craeting menu for students of some facility and gathering there information
def menu():
    print("[1]option 1 (adding astudent)")
    print("[2]option 2 (search a student)")
    print("[3]option 3 (delete student)")
    print("[4]option 4 (edit student information)")
    print("[5]option 5 (exit the program)")

students = []

while True:
    menu()
    option = int(input("please enter number of your option: "))

    match option:
        case 1:
            name = input("please enter student name: ")
            age = int(input("please enter student age: "))
            student_ID = int(input("please enter student ID: "))
            student = {
                "name": name,
                "age": age,
                "student ID": student_ID,
            }
            students.append(student)
            print("student added to the program")
        case 2:
            student_ID = int(input("please enter student ID: "))
            for student in students:
                if student["student ID"] == student_ID:
                    print("student has found")
                    print(student)
                    break
            else:
                print("student has not found")
        case 3:
            student_ID = int(input("enter student ID delete student: "))
            for student in students:
                if student["student ID"] == student_ID:
                    students.remove(student)
                    print("student has been deleted")
                    break
            else:
                print("student has not found")
        case 4:
            student_ID = int(input("please enter student ID: "))
            for student in students:
                if student["student ID"] == student_ID:
                    student["name"] = input("please enter new name: ")
                    student["age"] = int(input("please enter new age: "))
                    print("student information has been updated")
                    break
            else:
                print("student has not found")
        case 5:
            print("thank you for using the program")
            break
        case _:
            print("not found option, choose from 1 to 5")

# saving the program in a file
with open("students.txt", "w") as file:
    file.write(str(students))