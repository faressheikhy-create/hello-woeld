# writing a calculator for basic operations so it can be used in other files (module)
def cal(num1, num2, opration):
    match opration:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case _:
            raise ValueError(f"Unsupported operation: {opration}")

def num_check(a):
    match a:
        case 0:
            return "number is zero"
        case 1:
            return "number is one"
        case a if a > 0:
            return "positive number"
        case a if a < 0:
            return "negative number"
        case _:
            return "not a number"
a = int(input("enter a number: "))
res = num_check(a)
print(res)