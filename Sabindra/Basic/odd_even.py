number = int(input("Enter a number: "))

def odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    

result = odd_even(number)
print(result)

