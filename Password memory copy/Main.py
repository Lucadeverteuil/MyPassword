
from email.header import Header
import pandas as pd 

while(True):
    try:
        check = pd.read_csv("MyPasswords.csv")
        break
    except Exception as e:
        print("File was empty")
        check = pd.DataFrame({"Web":["Website"], "user": ["Username"], "pass": ["Password"]})
        check.to_csv("MyPasswords.csv", header=False,index = False, sep="\t")
        break

class Account: 
    def __init__(self,Website, Username, Password):
        self.Username = Username
        self.Password = Password
        self.Website = Website
        self.df = pd.DataFrame()
    def Add_To_Csv(self): 
        add = ({'Website': [self.Website], 'Username': [self.Username], 'Password': [self.Password]})
        self.df = pd.DataFrame(add)
        self.df.to_csv("MyPasswords.csv", mode = 'a',header=False, index = False , sep= "\t")
print("Welcome to MyPasswords Luca. ")
while(True): 
    answer = input("What can I do for you today? 1.) find account, 2.) add account 3.)delet account 4.)edit account 5. Exit")
    read = pd.read_csv("MyPasswords.csv", sep= "\t")
    if answer == "1": 
        ans1 = input("Would you like 1.)a list of all your passwords or would you like 2.) to search")
        if ans1 == "1":
            print(read)
        elif ans1 == "2":
            ans2 = input("search: ")
            count = 0
            for i in read["Website"]:
                if ans2.lower() in i.lower():
                    print(read.loc[[count]])
                    count = count +1
                else:
                    count = count + 1
    elif answer == "2":
        Web = input("What is the Account name?")
        User = input("what is your user name? ")
        Pass = input ("What is your password? ")
        newAcc = Account(Web, User, Pass)
        newAcc.Add_To_Csv()
        print("Your account for " + Web + " has been added")
    elif answer == "3": 
         print(read)
         ans1 = input("Which Account would you like to remove? (Choose Number)")
         print(read.loc[int(ans1)])
         placeHold = input("Are you sure you want to delete?: ")
         if placeHold == "yes" or placeHold == "Yes":
             print("it has been Deleted:")
             read.drop([int(ans1)],inplace=True)
             read.to_csv("MyPasswords.csv", index= False, sep="\t")
    elif answer == "4": 
        print(read)
        ans1 = input("Which Account would you like to edit?(Chooose Number): ")
        print(read.loc[int(ans1)])
        ans2 = input("What do you want to edit: 1.) WebsiteName , 2.) UserName , 3.) Password: ")
        if ans2 == "1":
            placeHold = input(" What would you like to change the Website to? ")
            read.loc[int(ans1),"Website"] = placeHold
            read.to_csv("MyPasswords.csv", index= False, sep="\t")
            print("Okay it has been changed")
        elif ans2 == "2": 
            placeHold = input(" What would you like to change the Username to? ")
            read.loc[int(ans1),"Username"] = placeHold
            read.to_csv("MyPasswords.csv", index= False, sep="\t")
            print("Okay it has been changed")
        elif ans2 == "3": 
            placeHold = input(" What would you like to change the Password to? ")
            read.loc[int(ans1),"Password"] = placeHold
            read.to_csv("MyPasswords.csv", index= False, sep="\t")
            print("Okay it has been changed")
    elif answer == "5": 
        print("bye")
        break

    