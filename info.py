# gathering student information by creating a system to get the incoming information of the student
# creating a couple of (input) commands to verify the student
student_information = {}

student_information["name"] = input("please enter your name: ")
student_information["last name"] = input("please enter your last name: ")
student_information["age"] = int(input("please enter your age: "))
student_information["grade"] = int(input("please enter your grade: "))
print("student information after gathering them" , student_information)
# checking university required grade to pass (the required grade is 60 to 100)
# and checking required grade to failed (the required grade is 50 to 0)
# and if student requires grade between 50 to 60 have to repeat the test
if 60 <= student_information["grade"] <= 100:
    student_information["status"] = "pass"
elif 50 <= student_information["grade"] < 60:
    student_information["status"] = "repeat"
elif 0 <= student_information["grade"] <= 50:
    student_information["status"] = "failed"
else:
    student_information["status"] = "fail"
print(student_information)

# now lets bring loop situation with (for) command to make multiple grading system
# applying for command for three subjects
student_subject_grade = {}
for i in range(3):
    subject = input(f"please enter subject {i + 1} name: ")
    student_subject_grade[subject] = int(input(f"please enter the grade for {subject}: "))
print("student subject grades:", student_subject_grade)
# bringing (if) command to qualify whether the student has passed or failed
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