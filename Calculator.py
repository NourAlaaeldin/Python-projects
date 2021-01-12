num1 = float(input("Please enter the first number: "))
operator = input("Please enter the operator: ")
num2 = float(input("Please enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("You must not divide a number by zero !!")
        exit()
    result = num1 / num2
else:
    print("Invalid operator !!")
    exit()

print("The result equals: ",result)