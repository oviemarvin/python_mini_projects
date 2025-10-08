print("welcome to Marvin\'s Python Mini ATM")

#list of account holders stored in a dictionary

accounts={
        "Rhoda":{ "pin": 1234, "balance":500000, "transaction_history":[]},
        "marvin":{"pin":1002, "balance":500000, "transaction_history":[] }

           }
current_user = None


    #define our functions

def check_balance():
        print(f"your current balance is #{accounts[current_user]["balance"]}")

def withdraw_money():

        amount=int(input("Enter amount to withdraw: "))
        
        balance = accounts[current_user]["balance"]
        if amount > balance:
            print("Insufficient Funds..")
        else:
            accounts[current_user]["balance"]= balance-amount

            accounts[current_user]["transaction_history"].append(f"Withdrew: - {amount}")
            print(f"Withdrawal Succesful...!   New balance is #{accounts[current_user]["balance"]}")

def deposit_money():
        amount=int(input("Enter amount to deposit: "))
        balance= accounts[current_user]["balance"]
        accounts[current_user]["balance"]= balance+amount
        accounts[current_user]["transaction_history"].append(f"Deposited: + {amount}")
        print(f"#{amount} Deposited Successfully! ")
        
def transaction_history():
        print("Transaction History")
        for history in accounts[current_user]["transaction_history"]:
            print("-", history)


    #asks user for pin as means of identifying who the user is
while True:
    try:
        pin =int(input("enter pin: "))

    except:
        print("Invalid Pin! Please try again...!")
        continue
        
    for name, data in accounts.items():
            if data["pin"] ==pin:
                current_user=name
                print(f"welcome {name}!")
                break
            
    if current_user:  
            break
    else:
             print("no record...")  
        
        
while True:            
            print("1. Check Blance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Transaction History")
            print("5. Exit")

            try:
                choice = int(input("Enter an option: "))
            except:
                print("enter a number!!!!!!")
                continue


            #calling our functions
            if choice==1:
                check_balance()
            elif choice==2:
                withdraw_money()
            elif choice==3:
                deposit_money()
            elif choice==4:
                transaction_history()
            elif choice==5:
                print("Thank you for using our software...! ")
                break
            else:
                print("option not recognized")







    
     


    