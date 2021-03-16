import random
import string

Departments = {
    #Departments and there short names:
    "Production": "PD",
    "Research and development": "RDaD",
    "Purchasing": "PCD",
    "Marketing and selling": "MSaD",
    "Human Rescource Management": "HRMD",
    "Accounting and Fiance": "AFaD",

}

userGmail = "@gmail.com"
userYahoo = "@yahoo.com"
userIcloud = "@iCloud.com"
userOutlook = "@outlook.com"

while True:
    print("-------------------------------")
    print("1: Make an email and password ")
    print("2: Change password ")
    print("3: See your passowrd and email" )
    print("-------------------------------")

    userInput = input("Write your choice: ")
    if userInput == "1":        
        userName = input("Write your name: ")
        if userName.islower() or userName.isupper() or userName == userName:
            newUserName = userName.title()
            print("")

        userSurname = input("Write your surname: ")
        if userSurname.islower() or userSurname.isupper() or userSurname == userSurname:
            newUserSurname = userSurname.title()
            print("")
        
        userDepartment = input("Write your department in the company: ")
        if userDepartment.islower() or userDepartment.upper() or userDepartment == userDepartment:
            newUserDepartment = userDepartment.title()
            print("")

        userEmail = newUserName + newUserSurname + newUserDepartment

        print("-----------------")
        print("1: " + userGmail)
        print("2: " + userYahoo)
        print("3: " + userIcloud)
        print("4: " + userOutlook) 
        print("-----------------")
        print("")
        userPick = input("Write your email ending choice: ")
        if userPick is userGmail or "1":
            finalUserEmail = userEmail + userGmail

        elif userPick is userYahoo or "2":
            finalUserEmail = userEmail + userYahoo

        elif userPick is userIcloud or "3":
            finalUserEmail = userEmail + userIcloud

        elif userPick is userOutlook or "4":
            finalUserEmail = userEmail + userOutlook
        
        print("Your new email is: " + finalUserEmail)
        print("")
        #Password with validation checks
        print("Lets make a secure password\n Your passowrd should be 10 characters long, have a capital letter and numbers")
        userPassword = input("Write your password: ")

        if len(userPassword) < 10 and len(userPassword) > 15:
            print("Your password is too short or too long! \n The max character limit is 15.")

        elif userPassword.islower() or userPassword.isupper():
            newUserPassowrd = userPassword.title()

    elif userInput == "2":
        changepass = input("Write your old password: ")
        if changepass == userPassword:
            ch = input("Change your password: ")
        elif changepass != userPassword:
            print("Try again!")
