password = input('Enter new password: ')
if password == "12345678" :
    print("-----------------Correct-----------------")
else:
    print("-------Inccorect password-------")
    forgot = input("Forgot password? [y/n]: ")
    if forgot == "y" :
        newpass = input('Enter new password: ')
        sure = input("Sure? [y/n] , " + newpass + ': ')
        if sure == "y":
            print("----Password changed----")
            password = input('Enter new password: ')
            if password == newpass :
               print("-----------------Correct-----------------")
            else:
                print("------Incorrect password------")
    else:
        print("...")