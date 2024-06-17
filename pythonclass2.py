# #Classwork from June 14 2024

# # # Example 1: Find the letter a in the input word
# # word = input("Please enter a word: ")
# # for character in word:
# #     if character=="a":
# #          print(f"There is an {character} inside the word")
# #     else:
# #         print(f"There is no {character} inside the word")

# # # Example 2:
# # i=0
# # while i==0:
# #     inputnumber=input("Please provide a number: ")
# #     inputnumber=int(inputnumber)
# #     if inputnumber%2==0:
# #         print(f"The number {inputnumber} is an even number")
# #     elif inputnumber%3==0:
# #         print(f"The number {inputnumber} is divisible by the number 3")
# #     elif inputnumber%5==0:
# #         print(f"The number {inputnumber} is divisible by the number 5")
# #     elif inputnumber%7==0:
# #         print(f"The number {inputnumber} is divisible by the number 7")
# #     else:
# #         print(f"Sorry the number is not divisible by either 1,3,5,7")
# #     inputcontinuity=input("Do you want to continue? type 'Y' or 'N' ")
# #     if inputcontinuity=='Y' or inputcontinuity=='y':
# #         continue
# #     else:
# #         i=1

# #Task 1: Create a function that takes an input from the user and fills up the whitespaces with + sign
# userinput1 = input("Please enter a sentence: ")
# def plus_sign(word):
#     return '+'.join(word.split())
# print(plus_sign(userinput1))

# #Task 2: Create a function that takes a number as an input from the user and checks if it is 
# # # lower than 500 but higher than 250
# userinput2 = int(input("Please enter a number: "))
# def number(num):
#     if num > 250 and num < 500:
#         return "The number is lower than 500 but higher than 250"
#     elif num < 250:
#         return "The number is less than 250"
#     else:
#         return "The number is greater than 500"
# print(number(userinput2))

#Task 3: Create an ATM  booth, where you cna deposit any amount of money,
# first step is to input your first name and last name and date of birth
#----After this step, put a prompt on what the user wants to do, for example say "Welcome Firstname, what would you like to do today? 1. Deposit 2. Withdraw 3. Take out the card"
# second step, it should promt you to provide if option 1 --> "How much money would you like to deposit?" 
# third step, after deposit, you can have withdraw option as well, if option 2 --> "How much money would you like to withdraw?"
# you need to also put a limit to withdrawal, you cannot withdraw more than you have in ATM or the limit of 500, maximum you can withdraw is 500
# if the user chooses option 3 --> print "Thank you so much, have a wonderful day Firstname"
userinput3_FirstName = input("Please input your first name: ")
userinput3_LastName = input("Please input your last name: ")
userinput3_DOB = int(input("Please input your birthdate (MMDDYYY): "))
userinput3_option = int(input(f"Welcome {userinput3_FirstName}, what would you like to do today? 1. Deposit 2. Withdraw 3. Take out the card: "))
i=0
option=0
deposit=0
total_deposit=0
while i==0:
    while userinput3_option != 3:
        if userinput3_option == 1:
            deposit = int(input("How much money would you like to deposit? "))
            total_deposit += deposit
            print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")

            while option != 3:
                option = int(input("Please input another option: 1. Deposit 2. Withdrawal 3. Take out the card: "))
                if option == 1:
                    deposit = int(input("How much money would you like to deposit? "))
                    total_deposit += deposit
                    print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")
                elif option ==2:
                    withdrawal = int(input("How much money would you like to withdraw? "))
                    if withdrawal > 500 or withdrawal > total_deposit:
                        print("You cannot withdraw more than the limit of 500 or than your account balance")
                    else:
                        total_deposit -= withdrawal
                        print(f"You have withdrawn {withdrawal} dollars. You now have {total_deposit} dollars in your account.")
                else:
                    userinput3_option = 3
                
        elif userinput3_option == 2:
            withdrawal = int(input("How much money would you like to withdraw? "))
            if withdrawal > 500 or withdrawal > total_deposit:
                print(f"Your current balance is {total_deposit}. You cannot withdraw more than the limit of 500 or than your account balance")
            else:
                print(f"Your current balance is {total_deposit}. You need to deposit money first.")

            while option != 3:
                option = int(input("Please input another option: 1. Deposit 2. Withdrawal 3. Take out the card: "))
                if option == 1:
                    deposit = int(input("How much money would you like to deposit? "))
                    total_deposit += deposit
                    print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")
                elif option ==2:
                    withdrawal = int(input("How much money would you like to withdraw? "))
                    if withdrawal > 500 or (withdrawal > total_deposit and total_deposit > 0):
                        print("You cannot withdraw more than the limit of 500 or than your account balance")
                    else:
                        total_deposit -= withdrawal
                        print(f"You have withdrawn {withdrawal} dollars. You now have {total_deposit} dollars in your account.")
                else:
                    userinput3_option = 3
       
    if userinput3_option == 3:
        print(f"Thank you so much, have a wonderful day {userinput3_FirstName}")
        i +=1

    
    
