a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator(+, -, *, /): ")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "error"
    
result = calculator(a, b, operator)
print(round(result,2)) 