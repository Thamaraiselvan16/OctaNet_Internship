import time

print("Please insert Your CARD")

time.sleep(5)

password=1234

print("----------------------------------------------------------------")
pin=int(input("Enter Your ATM pin : "))
print("----------------------------------------------------------------")

balance=5000

if pin==password:
    while True:
        
        print("""
            1. Balance
            2. Withdraw Balance
            3. Deposit Balance
            4. Exit
            """)
        try:
            print("----------------------------------------------------------------")
            option=int(input("Please enter your choice: "))
            print("----------------------------------------------------------------")
        except:
            print("Please enter valid option: ")
            
        
        if option==1:
            print("----------------------------------------------------------------")
            print(f"Your current balance is {balance}")
            print("----------------------------------------------------------------")
            
        if option==2:
            print("----------------------------------------------------------------")
            withdraw_amount=int(input("Please Enter withdraw amount: "))
            print("----------------------------------------------------------------")
            balance=balance-withdraw_amount
            
            print(f"{withdraw_amount} is debited from your account")
            print("----------------------------------------------------------------")
            print(f"Your updated balance is {balance}")
            print("----------------------------------------------------------------")
            
        if option==3:
            print("----------------------------------------------------------------")
            deposit_amount=int(input("Please Enter a deposit amount: "))
            print("----------------------------------------------------------------")
            
            balance=balance+deposit_amount
            
            print("----------------------------------------------------------------")
            print(f"{deposit_amount} is credited to your account")
            print("----------------------------------------------------------------")
            
            print("----------------------------------------------------------------")
            print(f"Your updated  balance is {balance}")
            print("----------------------------------------------------------------")
            
        if option==4:
            print("----------------------------------------------------------------")
            print("thank you for visit ATM")
            print("----------------------------------------------------------------")
            break
        

else:
    print("----------------------------------------------------------------")
    print("Wrong pin please try again")
    print("----------------------------------------------------------------")
    
        
        
        
        
        