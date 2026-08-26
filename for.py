# loop functions in (for) command for odd numbers , pair numbers , multiplication , addition
# print odd numbers
for i in range(1, 16):
    if i % 2 != 0:
        print(i)
# print pair numbers
for i in range(1, 16):
    if i % 2 == 0:
        print(i)
# print addition of numbers
total = 0
for i in range(1, 11):
    total = total + i
    print(total)

# print multiplication of numbers
total = 1
for i in range(1, 9):
    total = total * i
    print(total)

# startin function with (for) loop for fibonacci series and factorial series
#  factorial series
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
    print("Factorial =", factorial)
# fibonacci series
a = 0
b = 1
for i in range(10):
    print(a)
    next_number = a + b
    a = b
    b = next_number