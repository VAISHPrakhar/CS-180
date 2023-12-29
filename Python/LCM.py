#calculating LCM of two numbers with user input
import math

def calculate_lcm_with_input():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    lcm = (x * y) // math.gcd(x, y)
    print(f"The LCM of {x} and {y} is {lcm}")
