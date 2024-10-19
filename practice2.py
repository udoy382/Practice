"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Operator: ")

if op == "+" or op == "add":
    print(num1 + num2)
elif op == "-" or op == "sub":
    print(num1 - num2)
elif op == "*" or op == "mul":
    print(num1 * num2)
elif op == "/" or op == "div":
    print(num1 / num2)
else:
    print("something wrong, please try again.")
"""

"""
def evenAndOdd(userInput):
    if userInput % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

userInput = int(input("Enter a number: "))
evenAndOdd(userInput)
"""

user = int(input("Enter a non-negative number : "))

if user <= 0:
    print("Oops! Something went wrong, Try again.")
else:
    n = []
    for digit in range(1, user + 1):
        n.append(digit)

    print(digit)

    print(n)