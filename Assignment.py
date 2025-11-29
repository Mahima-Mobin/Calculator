def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
def add():
    a = get_number("Enter a number: ")
    b = get_number("Enter another number: ")
    r = a + b
    print(f"{a} + {b} = {r}")
    menu()
def substract():
     a = get_number("Enter a number: ")
     b = get_number("Enter another number: ")
     r = a - b
     print(f"{a} - {b} = {r}")
     menu()
def multiply():
     a = get_number("Enter a number: ")
     b = get_number("Enter another number: ")
     r = a * b
     print(f"{a} * {b} = {r}")
     menu()
def divide():
    try:
        a = get_number("Enter a number: ")
        b = get_number("Enter another number: ")
        r = a / b
        print(f"{a} / {b} = {r}")
        menu()
    except ZeroDivisionError:
        print("Can't divide by Zero.")
        menu()

def menu():
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        add()
    elif choice == 2:
        substract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        exit
    else:
        print("Invalid Choice!")
menu()

