from turtle import bye
import pandas as pd 

class Account: 
    def __init__(self,Website, Username, Password):
        self.Username = Username
        self.Password = Password
        self.Website = Website
    def Add_To_Csv(self): 
        df = pd.DataFrame([[self.Website, self.Username, self.Password]], columns=["Website", "UserName", "Password"])
        df.to_csv("MyPasswords.csv", index = False, sep= "\t")

        
    

    
print("Welcome to MyPasswords Luca. ")
while(True): 
    answer = input("What can I do for you today? 1.) find account, 2.) add account 3.)delet account 4.)edit account 5. Exit")
    read = pd.read_csv("MyPasswords.csv", sep= "\t")
    if answer == "2":
        Web = input("What is the Account name?")
        User = input("what is your user name? ")
        Pass = input ("What is your password? ")
        newAcc = Account(Web, User, Pass)
        newAcc.Add_To_Csv()
        print("Your account for " + Web + " has been added")
    elif answer == "1": 
        ans1 = input("Would you like 1.)a list of all your passwords or would you like 2.) to search")
        if ans1 == "1":
            print(read)
        elif ans1 == "2":
            ans2 = input("search: ")
            for i in read["Website"]:
                if ans2.lower() in i.lower():
                    print(i)
    elif answer == "5": 
        print("bye")
        break