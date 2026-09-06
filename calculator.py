# Calculator functions
def sum_n(num1, num2):
    return num1 + num2
def sub_n(num1, num2):
    return num1 - num2
def mult_n(num1, num2):
    return num1 * num2
def div_n(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2
def power_n(num1, num2):
    return num1 ** num2
def mod_n(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 % num2
def floor_div_n(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 // num2

# Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show calculator menu
print("\nChoose an operation:")
print("+   Addition")
print("-   Subtraction")
print("*   Multiplication")
print("/   Division")
print("**  Power")
print("%   Modulus")
print("//  Floor division")
operation = input("Enter operation: ")

# Perform calculation using keyword arguments
if operation == "+":
    result = sum_n(num1=num1, num2=num2)
elif operation == "-":
    result = sub_n(num1=num1, num2=num2)
elif operation == "*":
    result = mult_n(num1=num1, num2=num2)
elif operation == "/":
    result = div_n(num1=num1, num2=num2)
elif operation == "**":
    result = power_n(num1=num1, num2=num2)
elif operation == "%":
    result = mod_n(num1=num1, num2=num2)
elif operation == "//":
    result = floor_div_n(num1=num1, num2=num2)
else:
    result = "Error: Invalid operation"
# Display result
print(f"\nResult: {result}")

# finding the area of a circle
def circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
circle_radius = float(input("Enter the radius of the circle: "))
result = circle_area(radius=circle_radius)
print(f"Area of the circle = {result}")