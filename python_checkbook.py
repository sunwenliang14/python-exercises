print('~~~ Welcome to your terminal checkbook! ~~~')

def menu():
    print('''What would you like to do?
    
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit''')  
menu()

    user_choice = input("Please choose a number between 1 and 4")
while (user_choice.isdigit() == False or int(user_choice) < 1    
            or int(user_choice) > 4 ):
        print(f"{user_choice} is nice, but please select a whole number between 1 and 4.")
        user_choice = input("Please input a whole number between 1 and 4.")

user_choice = int(user_choice)
current_banlance = 1000
if user_choice == 1:
        print(f'Your current balance is {current_balance}')
        


    