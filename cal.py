# writing a calculator for basic operations so it can be used in other files (module)
def cal(num1, num2, opration):

    if opration == "+":
        result = num1 + num2
    elif opration == "-":
        result = num1 - num2
    elif opration == "*":
        result = num1 * num2
    elif opration == "/":
        result = num1 / num2
    elif opration == "**":
        result = num1 ** num2
    else:
        raise ValueError(f"Unsupported operation: {opration}")
    return result
    
