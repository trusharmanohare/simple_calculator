#####
# creating simple calculator using python operators #
# #####

# creating a menu list -->
print("Operation Menu:")
print("1. Addition:")
print("2. subtraction:")
print("3. divided:")
print("4. multiple:")
print("5. power:")
print("6. percentage:")

# creating a object -->
user = int(input("Enter the operation number: "))

# creating two variables -->
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))

# addition of two numbers -->
if user == 1:
    Addition = num1 + num2
    print(num1 + num2)

# subtraction of two numbers -->
elif user == 2:
    subtraction = num1 - num2
    print(num1 - num2)

# divided of two numbers -->
elif user == 3:
    divided = num1 / num2
    print(num1 / num2)

# multiple of two numbers -->
elif user == 4:
    multiple = num1 * num2
    print(num1 * num2)

# power of two numbers -->
elif user == 5:
    power = num1 ** num2
    print(num1 ** num2)
# percentage of two numbers -->
elif user == 6:
    print((num1 / num2) * 100)
else:
    print("Enter valid Input")
