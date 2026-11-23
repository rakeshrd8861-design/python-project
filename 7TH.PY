def greet (name):
    print(f"Hello , {name}! How do you do?")
greet("Alice")
greet("mubarak")
greet("rakesh")



def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)


def multiply(a, b):
    return a * b
result = multiply(5, 3)
print("The product is:", result)

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"    


def power(base, exponent=2):
    return base ** exponent     
result = power(5, 3)
print("The power is:", result)
print(power(5))