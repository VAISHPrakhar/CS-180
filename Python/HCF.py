#hcf of two numbers using def function
def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))
