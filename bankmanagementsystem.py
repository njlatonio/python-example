i = 0
j = 0
while i == 0:
    option1 = int(input("Welcome to Beautiful Canada Bank! Please select an option: 1. Create a chequing account 2. Create a savings account: "))
    if option1 == 1 or option1 ==2:
        userinput3_FirstName = input("Please input your first name: ")
        userinput3_LastName = input("Please input your last name: ")
        userinput3_DOB = int(input("Please input your date of birth (DDMMYYYY): "))
        print("Congratulations! You have joined Beautiful Canada Bank.")
        print(f"Your user ID is BCB0000{j}")
        j += 1
        userinput3_option = int(input(f"Please select one of the following options to 1. Deposit 2. Withdraw 3. Remove ATM Card: "))
        k=0
        option=0
        deposit=0
        total_deposit=0
        withdrawal_limit = 1000
        while k==0:
            while userinput3_option != 3:
                if userinput3_option == 1:
                    deposit = int(input("How much money would you like to deposit? "))
                    total_deposit += deposit
                    print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")

                    while option != 3:
                        option = int(input("Please input another option: 1. Deposit 2. Withdrawal 3. Remove ATM Card: "))
                        if option == 1:
                            deposit = int(input("How much money would you like to deposit? "))
                            total_deposit += deposit
                            print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")
                        elif option ==2:
                            withdrawal = int(input("How much money would you like to withdraw? "))
                            if withdrawal > withdrawal_limit or withdrawal > total_deposit:
                                print(f"You cannot withdraw more than the limit of {withdrawal_limit} or than your account balance")
                                
                                m = 0
                                while m == 0:
                                    limit_option = input("Would you like to increase the withdrawal limit? Maximum limit is 5000. (Y/N): ")
                                    if limit_option == "Y" or limit_option == "y":
                                        limit_amount = int(input("Please input the new withdrawal limit. (Max 5000):" ))
                                        withdrawal_limit = limit_amount
                                        print(f"Your new withdrawal limit is {withdrawal_limit}")
                                        m += 1
                                    elif limit_option == "N" or limit_option == "n":
                                        print(f"Your withdrawal limit remains at {withdrawal_limit}")
                                        m += 1
                                    else:
                                        print("Please enter a valid option (Y/N): ")    
                            else:
                                total_deposit -= withdrawal
                                print(f"You have withdrawn {withdrawal} dollars. You now have {total_deposit} dollars in your account.")
                        else:
                            userinput3_option = 3
                        
                elif userinput3_option == 2:
                    withdrawal = int(input("How much money would you like to withdraw? "))
                    if withdrawal > withdrawal_limit or withdrawal > total_deposit:
                        print(f"Your current balance is {total_deposit}. You cannot withdraw more than the limit of {withdrawal_limit} or than your account balance")
                        
                        m = 0
                        while m == 0:
                            limit_option = input("Would you like to increase the withdrawal limit? Maximum limit is 5000. (Y/N): ")
                            if limit_option == "Y" or limit_option == "y":
                                limit_amount = int(input("Please input the new withdrawal limit. (Max 5000):" ))
                                withdrawal_limit = limit_amount
                                print(f"Your new withdrawal limit is {withdrawal_limit}")
                                m += 1
                            elif limit_option == "N" or limit_option == "n":
                                print(f"Your withdrawal limit remains at {withdrawal_limit}")
                                m += 1
                            else:
                                print("Please enter a valid option (Y/N): ")                          
                                            
                    else:
                        print(f"Your current balance is {total_deposit}. You need to deposit money first.")

                    while option != 3:
                        option = int(input("Please input another option: 1. Deposit 2. Withdrawal 3. Remove ATM Card: "))
                        if option == 1:
                            deposit = int(input("How much money would you like to deposit? "))
                            total_deposit += deposit
                            print(f"You have deposited {deposit} dollars in your account. You now have {total_deposit} dollars in your account. Thank you!")
                        elif option ==2:
                            withdrawal = int(input("How much money would you like to withdraw? "))
                            if withdrawal > withdrawal_limit or (withdrawal > total_deposit and total_deposit > 0):
                                print(f"You cannot withdraw more than the limit of {withdrawal_limit} or than your account balance")
                            
                                m = 0
                                while m == 0:
                                    limit_option = input("Would you like to increase the withdrawal limit? Maximum limit is 5000. (Y/N): ")
                                    if limit_option == "Y" or limit_option == "y":
                                        limit_amount = int(input("Please input the new withdrawal limit. (Max 5000):" ))
                                        withdrawal_limit = limit_amount
                                        print(f"Your new withdrawal limit is {withdrawal_limit}")
                                        m += 1
                                    elif limit_option == "N" or limit_option == "n":
                                        print(f"Your withdrawal limit remains at {withdrawal_limit}")
                                        m += 1
                                    else:
                                        print("Please enter a valid option (Y/N): ")
                            else:
                                total_deposit -= withdrawal
                                print(f"You have withdrawn {withdrawal} dollars. You now have {total_deposit} dollars in your account.")
                        else:
                            userinput3_option = 3
            
            if userinput3_option == 3:
                b = 0
                while b == 0:
                    final_option = input("Before leaving, would you like to create another chequing or savings account? (Y/N): ")
                    if final_option == "Y" or final_option == "y":
                        b += 1
                        k += 1
                        i = 0
                    elif final_option == "N" or final_option == "n":
                        print(f"Thank you so much for vising Beautiful Canada Bank, have a wonderful day {userinput3_FirstName}!")
                        b +=1
                        k +=1
                        i +=1
                    else:
                        print("Please enter a valid option (Y/N): ")
                

    
    else:
        quit_option = input("Please select a valid option and enter any key to return to main menu or enter 'quit' to leave: ")
        if quit_option == "quit":
            i +=1
        else:
            i = 0