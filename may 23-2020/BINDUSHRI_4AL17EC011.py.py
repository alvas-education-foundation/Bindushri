name = input("enter the username:")
credential = input("enter the password:")

if credential == 'e3$WT89x' and name == 'Micheal':
    print("your login is succefull")

flag = 0
while flag <3:
    if credential != 'e3$WT89x' or name != 'Micheal':
        print("username and password is invalid")
        break
flag+=1
name = input("enter the username: ")
credential = input("enter the password: ")
if credential == 'e3$WT89x' and name == 'Micheal':
    print("your login is succesfull")
if flag==2:
    print("account locked")