#Mini ATM Simulation
import getpass
pin="1234"
Balance=50000
attempts=3

while attempts>0:
    enter_pin=getpass.getpass("enter your pin=")
    if(enter_pin==pin):
        print("login successful")


        while True:

          print("Welcome to canara bank ATM",)
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
                break
    
          else:
           print("Invalid choice ,please try again. ")
        break 
    else:
        attempts-=1
        print("Incorrect pin!",attempts,"attempts are left")
        if (attempts==0):
            print("your card has been blocked,please contact your bank")  