# print("Hello World")

# #To create a function
# def greet(name):
#     return f"Hello {name}!"
# print(greet("Alice"))

# if 5 > 2:
#   print("Five is greater than two!")

# x = 5
# y = "John"
# print(x)
# print(y)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# #Random example
# def amount_money(cash):
#     return f"I have {cash} dollars"
# print(amount_money(1000))

# #Other example
# def name_money_example(money, name1):
#     return f"Hello {name1}, here is {money} dollars."
# print(name_money_example(5000,"Nichelle"))

# def calculate_sum(numbers):
#     return(sum(numbers))
# #1st step
# input_numbers= input("Enter numbers seperated by spaces: ")
# #2nd step
# after_split = input_numbers.split()
# after_map = map(int, after_split)
# after_list = list(after_map)
# print(after_split)
# print(after_map)
# print(after_list)
# #3rd step
# numbers_list = list(map(int, input_numbers.split()))
# print(numbers_list)
# #4th step
# total_sum = calculate_sum(numbers_list)
# print("The sum of the numbers is:", total_sum)

#Substraction and multiplication function
# 1. sum function
# 2. substraction function
# 3. multiplication function

# Request the user for 2 inputs, put thiis in a variable enter first/second number

# input_number1 = int(input("Please input a number: "))
# input_number2 = int(input("Please input another number: "))
# sum = input_number1 + input_number2
#print("The sum of both numbers are " + f"{sum}")

input_number1 = int(input("Please input a number: "))
input_number2 = int(input("Please input another number: "))
def sum_numbers(number1, number2):
    return f"The addition of both numbers are {number1 + number2}"
print(sum_numbers(input_number1,input_number2))

def subtract_numbers(number1, number2):
    if number1 < number2:
        return "Sorry number 1 is smaller than number 2"
    else:
        return f"The substraction of both numbers are {number1 - number2}"
print(subtract_numbers(input_number1,input_number2))

def multiplication_numbers(number1, number2):
    return f"The multiplication of both numbers are {number1*number2}"
print(multiplication_numbers(input_number1,input_number2))