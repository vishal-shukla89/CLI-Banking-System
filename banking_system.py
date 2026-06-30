import random
import string
from pathlib import Path
import json

class Bank:
    database='data.json'
    data=[]        #it is empty dummy list 
    try:
        if Path(database).exists():    #it is to check if file eixsts or not
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("data.json file does not exists")
    except Exception as err:
        print(f"An error occured as {err}")

    #to create an update function which dumps dummy data ino data.json
    @classmethod
    def __update(cls):
        with open(Bank.database,"w") as fs:
            fs.write(json.dumps(Bank.data,indent=4))

    #to create a function which generates random account munber of 6-digits,3-chra,1-special chara
    @classmethod
    def __genrateAccNum(cls):
        while True:
            digit=random.choices(string.digits,k=6)
            char=random.choices(string.ascii_letters,k=3)
            spchar=random.choices("!@#$%&*")
            id=digit + char + spchar
            random.shuffle(id)
            id="".join(id)
            for i in Bank.data:
                if i["accnum"]==id :
                    break
            else:
                    return id
                    
    #to create function for creating new account
    def createaccount(self):
        info={
            "name":input("Enter Your Full Name :- "),
            "age":int(input("Enter Your Age :- ")),
            "email":input("Enter Youe Email :- "),
            "pin":int(input("Enter your 4 digits pin :- ")),
            "accnum":self.__genrateAccNum(),
            "balance":0
        }
        if info["age"]<18 or len(str(info["pin"]))!=4:
            print("Sorry you cant create your account!!!")
        else:
            print("YOUR ACCOUNT SUCCESSFULLY CREATED !!")
            print("Your account details are:- \n")
            for i in info:
                print(f"{i}:{info[i]}")
            Bank.data.append(info)
            Bank.__update()

    #to creating a function to deposite money
    def depositemoney(self):
        accnum=input("Enter your account number :- ")
        pin=int(input("Enter your pin:- "))
        userdata=[i for  i in Bank.data if i["accnum"]==accnum and i["pin"]==pin]
        
        # PRO TWEAK: Changed userdata==False to not userdata
        if not userdata:
            print("Sorry your pin or account number is wrong!!!!")
        else:
            amt=int(input("Enter the amount you want to deposite:- "))
            if amt>10000 or amt<0:
                print("Sorry amount is not in between 1-10000")
            else:
                userdata[0]["balance"]+=amt
                Bank.__update()
                print("AMOUNT DEPOSITED SUCCESSFULLY !!!")

    #to create a function which withdraws money
    def withdrawmoney(self):
        accnum=input("Enter your account number :- ")
        pin=int(input("Enter your pin:- "))
        userdata=[i for  i in Bank.data if i["accnum"]==accnum and i["pin"]==pin]
        
        # PRO TWEAK: Changed userdata==False to not userdata
        if not userdata:
            print("Sorry your pin or account number is wrong!!!!")
        else:
            amt=int(input("Enter the amount you want to withdraw:- "))
            if amt>userdata[0]["balance"]:
                print("Sorry amount is not in range of your balance")
            else:
                userdata[0]["balance"]-=amt
                Bank.__update()
                print("AMOUNT WITHDREAWN SUCCESSFULLY !!!")

    #to create a function which shows details of account
    def details(self):
        accnum=input("Enter your account number :- ")
        pin=int(input("Enter your pin:- "))
        userdata=[i for  i in Bank.data if i["accnum"]==accnum and i["pin"]==pin]
        
        # PRO TWEAK: Changed userdata==False to not userdata
        if not userdata:
            print("Sorry your pin or account number is wrong")
        else:
            print("Your Details Are As Follow:-\n")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")
    
    #to create a function to update details like name, email, pin only
    def updatedetails(self):
        accnum=input("Enter your account number :- ")
        pin=int(input("Enter your pin:- "))
        userdata=[i for  i in Bank.data if i["accnum"]==accnum and i["pin"]==pin]
        
        # PRO TWEAK: Changed userdata==False to not userdata
        if not userdata:
            print("Sorry Your pin or email is wrong")
        else:
            print("YOU CANNOT CHANGE AGE,ACCOUNT NUMBER,BALANCE\n")
            print("fill the details for change or leave it blank if no changes")
            newdata={
                "name":input("Enter your new name :- "),
                "email":input("Enter your new mail:- "),
                "pin":input("enter your new 4 digit pin :- "),
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]["name"]
            if newdata["email"]=="":
                newdata["email"]=userdata[0]["email"]
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]["pin"]
            
            newdata["age"]=userdata[0]["age"]
            newdata["accnum"]=userdata[0]["accnum"]
            newdata["balance"]=userdata[0]["balance"]
            if type(newdata["pin"])==str:
                newdata["pin"]=int(newdata["pin"])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            Bank.__update()
            print("DETAILS UPDATED SUCCESSFULLY !!")

    #to create a function which deletes the account
    def deleteaccount(self):
        accnum=input("Enter your account number :- ")
        pin=int(input("Enter your pin:- "))
        userdata=[i for  i in Bank.data if i["accnum"]==accnum and i["pin"]==pin]
        
        # PRO TWEAK: Changed userdata==False to not userdata
        if not userdata:
            print("Sorry Your pin or email is wrong")
        else:
            check=input("Press Y if you actually wants to DELETE account or Press N :- ")
            if check=="n" or check=="N":
                print("BYPASSED")
            else:
                index=Bank.data.index(userdata[0])
                v=Bank.data.pop(index)
                Bank.__update()
                print("ACCOUNT DELETED SUCCESSFULLY!!")

user=Bank()

# PRO TWEAK: Added 'while True' loop so the app stays open. Added option 7 to break the loop.
while True:
    print("\nPress 1 to create a new account ")
    print("Press 2 to deposite money into bank ")
    print("Press 3 to withdraw money from the account")
    print("Press 4 to see details of the account")
    print("Press 5 to update details of account")
    print("Press 6 to delete your account ")
    print("Press 7 to EXIT ")

    check=int(input("\nEnter your response between 1 to 7 :- "))

    if check==1:
        user.createaccount()
    elif check==2:
        user.depositemoney()
    elif check==3:
        user.withdrawmoney()
    elif check==4:
        user.details()
    elif check==5:
        user.updatedetails()
    elif check==6:
        user.deleteaccount()
    elif check==7:
        print("Thank you for using the Bank!")
        break
