print("\n******************* Python Default Calculator *******************")

# Variable that stores the choice of operation
print("\nAvailable operations:\n")
print("\n1 - Sum")
print("\n2 - Subtraction")
print("\n3 - Multiplication")
print("\n4 - Division\n")

option = input("\nChoice an operation (1/2/3/4): ")

# Functions of the sum
def sumFunction():
    first = int(input("\nType the first number: "))
    second = int(input("\nType the second number: "))
    sumResult = first + second
    print("\nThe sum between {0} e {1} is: ".format(first,second), sumResult)
    return;

def subtractionFunction():
    first = int(input("\nType the first number: "))
    second = int(input("\nType the second number: "))
    subtractionResult = first - second
    print("\nThe subtraction between {0} e {1} is: ".format(first,second), subtractioniResult)
    return;

def multiplicationFunction():
    first = int(input("\nType the first number: "))
    second = int(input("\nType the second number: "))
    multiplicationResult = first * second
    print("\nThe multiplication between {0} e {1} is: ".format(first,second), multiplicationResult)
    return;

def divisionFunction():
    first = int(input("\nType the first number: "))
    second = int(input("\nType the second number: "))
    division = first / second
    print("\nThe division between {0} e {1} is: ".format(first,second), divisionResult)
    return;

# Operation to validate the choosen option on input
if option == '1':
    sumFunction()
elif option == '2':
    subtractionFunction()
elif option == '3':
    multiplicationFunction()
elif option == '4':
    divisionFunction()
else:
    print("\nInvalid option for the operations displayed. Try again!")
