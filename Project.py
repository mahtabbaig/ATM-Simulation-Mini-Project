#Mini ATM Simulation

Balance=50000
name= input("Enter your name:")



     
    
    
    

        
print("Welcome to canara bank ATM",name)
print("1.Check balance")
print("2.Deposit money")
print("3.Withdraw money")
print("4.Exit")

choice=int(input("Enter your choice (1/2/3/4):"))

if(choice==1):

    print("Your balance =",Balance,"\nThank you visit again")

elif(choice==2):
    deposit=int(input("Enter amount of deposit:")) 
    Balance +=deposit
    print("Deposit is successfully done.\nNew balance:",Balance,"\nThank you visit again") 
elif(choice==3):
    withdraw=int(input("Enter amount of money to withdraw:"))   
    if (withdraw <=Balance ):

        Balance-=withdraw
        print("Withdraw is successfully done.\nNew balance:",Balance,"\nThank you visit again")
    else:
        print("Balance Unsuffient!") 

elif(choice==4):
     print("Thank you to visit canara bank ATM.")
    
     
    
         
else:
    print("Invalid choice ,please try again. ")