import csv
import details

def admin_login():
    print("Enter Credentials:")
    user_id = input("Username>> ")
    password = input("Password>> ")
    with open("admin_ID.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                if row[1] == password:
                    print("Log in Success")
                    file.close()
                    import Admin
                    return 0
                else:
                    print("Incorrect Info")
                    file.close()
                    return 1
            else:
                print("Incorrect Info")
                file.close()
                return 1


def user_login():
    user_id = input("Username>> ")
    password = input("Password>> ")
    with open("users_ID.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                if row[1] == password:
                    print("Login Success")
                    file.close()
                    import User
                    return 0
                else:
                    print("Incorrect Info")
                    file.close()
                    return 1
        print("Incorrect info")
        file.close()
    
def new_user():
    user_id = input("Enter Username>> ")
    with open("users_ID.txt",'r') as file:
        f = csv.reader(file)
        for row in f:
            if row[0] == user_id:
                print("This user already exist choose another one.")
                file.close()
                return new_user()
        file.close()
    password = input("Create a password>> ")
    name_ = details.name()
    contact_ = details.contact()
    blood_ = details.blood()
    f = open("users_ID.txt",'a')
    f.write(f"\n{user_id},{password},{name_},{contact_},{blood_}")
    f.close()
    print("Sign Up Success")
    print("Login to proceed")


def Login():
    print("1.Login as a USER")
    print("2.Login as ADMIN")
    print("3.New User? Sign up now !")
    print("4.Quit App")
    i = (int)(input("Your choice>> "))
    if i == 1:
        if (user_login()):
            print("1.please try again")
            print("2.Go to Login page")
            j = (int)(input("Your choice>> "))
            if j == 1:
                if (user_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid choice")
                Login()
    elif i == 2:
        if (admin_login()):
            print("1.Please try again")
            print("2.Go to login page")
            j = (int)(input("Your choice>> "))
            if j == 1:
                if (admin_login()):
                    Login()
            elif j == 2:
                Login()
            else:
                print("Invalid choice...")
                Login()
    elif i == 3:
        new_user()
    elif i == 4:
        quit()
    else:
        print("Please Enter a valid option")


while(1):
    Login()