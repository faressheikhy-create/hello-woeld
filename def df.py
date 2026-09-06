# defualt parameter
def hello(user="guest"):
    print(user)

hello()
# hello("shayan")
# key word argument
def std (name , age):
    print(name)
    print(age)

# std(age=20 , name="shayan")
std ("shayan", 23)
# calculater program writting
def sum_n(num1 , num2):
    total = num1 + num2
    return total
def sub_n(num1 , num2):
    sub = num1 - num2
    return sub
def mult_n(num1 , num2):
    mult = num1 * num2
    return mult
def div_n(num1 , num2):
    div = num1 / num2
    return div

sum_n(10 , 2)
sub_n(10 , 5)
mult_n(10 , 6)
div_n(10 , 2)
s = sum_n(10 , 2)
su = sub_n(10 , 5)
m = mult_n(10 , 6)
d = div_n(10 , 2)
print(f"sum={s} and sub={su} and mult={m} and div={d}")
# writting a function to take three numbers and print the avreage of them
def avreage(num1 , num2 , num3):
    avg = (num1 + num2 + num3)
    return avg / 3
avg = avreage(10,5,20)
print(f"avreage of three numbers is {avg}")
# calling the same function with keyword arguments
avg = avreage(num1=10 , num2=5 , num3=20)
print(f"avreage of three numbers is {avg}")