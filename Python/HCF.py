#program for calculating HCF of two numbers in a shorter way
def calculate_hcf(num1, num2):
    x = num1
    y = num2
    while(y):
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = calculate_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}")
