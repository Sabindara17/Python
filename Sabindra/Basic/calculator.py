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
    
button = True
while button:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    operator = input("Enter the operator(+, -, *, /): ")  
    result = calculator(a, b, operator)
    print(round(result,2)) 
    ans = input("Do you want to turn off? ")
    if ans.lower() == "yes":
         button = False

