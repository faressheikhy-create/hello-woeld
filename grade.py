# student information name,last name,age,current grade
student_name = "ali"
student_last_name = "gholi"
student_age = 20
grade = 16
# required grade to pass the course is 18
# requirements: check if the student grade is valid
if grade <= 18 and grade >= 13:
    print("The student grade is valid.")
elif grade < 13:
    print("The student grade is invalid.")
else:
    print("The student grade is not valid.")
if grade < 10:
    print("The student grade is very low and failed.")
elif grade >= 10 and grade < 13:
    print("The student grade is acceptable but low.")
else:
    print("The student grade is good.")
if grade < 10: 
    print("The student is failed.")
elif grade >= 10 and grade <= 18:
    print("The student is passed.")
# student is passed the course

#takin two numbers from user and create a loop to print all the numbers between them
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while num1 <= num2:
    print(num1)
    num1 += 1