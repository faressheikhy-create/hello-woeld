# writing a student info program (just like info.py project that i had wrote) to gather student information by using (def) command
# checking university required grade to pass (the required grade is 60 to 100)
# and checking required grade to failed (the required grade is 50 to 0)
# and if student requires grade between 50 to 60 have to repeat the test
def gather_student_info():
    student_information ={}
    student_information["name"] = input("please enter your name: ")
    student_information["lastname"] = input("please enter your lastname: ")
    student_information["age"] = int(input("please enter your age:" ))
    student_information["grade"] = int(input("please enter your grade: ")) 
    print("student information after gathering them", student_information)

    if 60 <= student_information["grade"] <= 100:
        student_information["status"] = "pass"
    elif 50 <= student_information["grade"] < 60:
        student_information["status"] = "repeat"
    elif 0 <= student_information["grade"] <= 50:
        student_information["status"] = "failed"
    else:
        student_information["status"] = "fail"
    print(student_information)
# now lets bring loop situation with (for) command to make multipule grading system
def gather_student_subject_grade():
    student_subject_grade = {}
    for i in range(3):
        subject = input(f"please enter subject {i + 1} name: ")
        student_subject_grade[subject] = int(input(f"please enter the grade for {subject}: "))
    print("student subject grades:", student_subject_grade)
    for subject, grade in student_subject_grade.items():
        if 60 <= grade <= 100:
            status = "passed"
        elif 50 <= grade < 60:
            status = "repeat"
        elif 0 <= grade <= 50:
            status = "failed"
        else:
            status = "invalid grade"
        print(f"{subject}: {status}")
# calling the functions to execute the program
gather_student_info()
gather_student_subject_grade()
# now lets bring return command to return the student information and student subject grades
def check_grade(grade):
    if 60 <= grade <= 100:
        return "pass"
    elif 50 <= grade < 60:
        return "repeat"
    elif 0 <= grade < 50:
        return "failed"
    else:
        return "invalid grade"

def get_student_information():
    student_information = {}

    student_information["name"] = input("Please enter your name: ")
    student_information["last_name"] = input("Please enter your last name: ")
    student_information["age"] = int(input("Please enter your age: "))
    student_information["grade"] = int(input("Please enter your grade: "))

    student_information["status"] = check_grade(
        student_information["grade"]
    )
    return student_information
student = get_student_information()
print("\nStudent Information:")
print(student)