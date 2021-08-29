import details

while (1):
    print("-+--+--+--+--+--+--+   Welcome to XYZ Blood Banks  -+--+--+--+--+--")
    print("+--+--+--+--+--+--+-        1.List of Donors      +--+--+--+--+--+-")
    print("+--+--+--+--+--+--+-         2.Add Hospital    +--+--+--+--+--+--+--")
    print("+--+--+--+--+--+--+-    3.View Hospital List    +--+--+--+--+--+--+--")
    print("+--+--+--+--+--+--+         4.User List         +-+--+--+--+--+--+--+")
    print("+--+--+--+--+--+--    5.Emergency Notifications  +--+--+--+--+--+--+-")
    print("+--+--+--+--+--+--+--            6.Quit          +--+--+--+--+--+--+-")
    i = (int)(input("Your choice>> "))
    if i == 1:
        print("1.Add a donor")
        print("2.View donor's list")
        print("3.View donor's with rare blood groups")
        j = (int)(input("Your choice>> "))
        if j == 1:
            details.Add_donor()
        elif j == 2:
            print("1.View all donor's")
            print("2.View donor's with a particular blood group")
            k = (int)(input("Your choice>> "))
            if k == 1:
                details.view_donor()
            if k == 2:
                details.donor_with_blood()
            else:
                print("Invalid choice")
        elif j == 3:
            print("donors of blood groups AB+ , AB- , B- are Shown below")
            details.view_donor_rare_blood()
        else:
            print("Invalid choice-2")
    elif i == 2:
        details.Add_hospital()
    elif i == 3:
        details.View_hospital()
    elif i == 4:
        details.view_user()
    elif i == 5:
        check = details.Emergency_check()
        if check != None:
            print("Emergency! There is a Blood Request")
            print("Patient Details:")
            print("Requied Blood Group:",check[0])
            print("Patient Name:",check[1])
            print("Contact No.:",check[2])
            print("Hospital Name:",check[3])
            print("Notifying Donors")
            details.donor_with_blood_help(check[0])
            print("Notifying Hosipitals and Blood banks press '1' if not required, or press anything else")
            a = (int)(input("Your choice:"))
            if a != 1:
                print("Below Hospitals and Blood banks are Notified")
                details.View_hospital()
            file = open("patients.txt",'a')
            file.write(f"\n{check[0]},{check[1]},{check[2]},{check[3]}")
            file.close()
            print("Patient details are succesfully added to the file 'patients.txt'")
        else:
            print("There are no Blood requests as of now")
    elif i == 6:
        quit()
    else:
        print("Invalid choice")









