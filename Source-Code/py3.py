import sys

user_data = "zjc"
user_pswd = "buaasem"
username = input("Username: ")

flag = True
wrong = 0
while flag:
    password = input("Password: ")
    if username == user_data:
        if(password == user_pswd):
            print("Welcome, login success")
            flag = False
            break
        else:
            print("try again, wrong password or username")
            wrong += 1
            if wrong == 3:
                sys.exit()
    else:
        print("Account not found")
        flag = False
        break
