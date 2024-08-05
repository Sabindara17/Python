# a = int(input("Enter the value of a: "))
# print(a)
# print(type(a))


# if a == 2:
#     print("it's correct")
# elif a == 1:
#     print("it's 1")
# else:
#     print("Nothing")

# age = int(input("Enter your age: "))

# if age <= 18 or age >= 50:
#     print("Not Allowed")
# else:
#     print("Allowed")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
operator = input("Enter the operator: ")

def calculator(a, b):
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


print(calculator)




