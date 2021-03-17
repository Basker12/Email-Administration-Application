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

print("-------------------------------")
print("1: Make an email and password ")
print("2: Change password ")
print("3: See your password and email" )
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

    userGmail = "@gmail.com"
    userYahoo = "@yahoo.com"
    userIcloud = "@iCloud.com"
    userOutlook = "@outlook.com"

    print("-----------------")
    print("1: " + userGmail)
    print("2: " + userYahoo)
    print("3: " + userIcloud)
    print("4: " + userOutlook)
    print("-----------------")
    print("")

    userPick = input("Write your email ending choice: ")
    if userPick == "1" or userPick == userGmail:
        finalUserEmail = userEmail + userGmail

    elif userPick == "2" or userPick == userYahoo:
        finalUserEmail = userEmail + userYahoo

    elif userPick == "3" or userPick == userIcloud:
        finalUserEmail = userEmail + userIcloud

    elif userPick == "4" or userPick == userOutlook:
        finalUserEmail = userEmail + userOutlook

    print("Your new email is: " + finalUserEmail)
    print("")


#Password with validation checks
randomNum = random.choice(string.ascii_letters)
randomNum2 = random.choice(string.ascii_letters)
randomNum3 = random.choice(string.ascii_letters)
randomNum4 = random.choice(string.ascii_letters)

randomNums = randomNum + randomNum2 + randomNum3 + randomNum4

userLength = False
while not userLength:
    userPassword = input("Write a pass: ")
    if len(userPassword) >= 10:
        userLength = True
        print("That's a good password: " + userPassword)
    else:
        print("Your password isn't 10 characters long, please try again.")

if userPassword.isupper() or userPassword.islower() or userPassword == userPassword:
    fUserPassword = userPassword.title()

finalUserPassword = fUserPassword + randomNums
print("This is your final password: " + finalUserPassword)
print("")
print(finalUserEmail)
print(finalUserPassword)


