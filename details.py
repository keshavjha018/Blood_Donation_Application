from datetime import date
import csv
import os

#hopitals.txt: hospital name,number,branch
#donors.txt: donor name,number,registered date,blood group
#blood_request.txt: blood type required,name,hospital,contact number

def Emergency_check():
    path = "blood_request.txt"
    if os.stat(path).st_size != 0:
        Blood_types = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
        with open("blood_request.txt", 'r') as file:
            check = csv.reader(file)
            for row in check:
                emergency = row
        open('blood_request.txt', 'w').close()
        if emergency[0] in Blood_types:
            return emergency
        return None
    else:
        return None

def name():
    name = input("Name:")
    return name

def contact():
    Contact = (int)(input("Contact Number:"))
    Contact_str = str(Contact)
    if len(Contact_str) == 10:
        return Contact
    print("Contact number must contain 10 digits only")
    return contact()

def blood():
    Blood = input("Blood Group:")
    Blood_types = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    if Blood in Blood_types:
        return Blood
    else:
        print("Please enter valid blood type.")
        return blood()

def view_user():
    with open("users_ID.txt", 'r') as file:
        donors = csv.reader(file)
        for row in donors:
            print("Name:",row[2],"Contact No:",row[3],"Blood Type:",row[4])
        file.close()

def view_donor():
    with open("donors.txt", 'r') as file:
        donors = csv.reader(file)
        for row in donors:
            print("Name:",row[0],"Contact No:",row[1],"Date joined:",row[2],"Blood Type:",row[3])
        file.close()

def view_donor_rare_blood():
    rare_blood = ["AB+","AB-","B-"]
    with open("donors.txt", 'r') as file:
        donors = csv.reader(file)
        for row in donors:
            if row[3] in rare_blood:
                print("Name:",row[0],"Contact No:",row[1],"Date joined:",row[2],"Blood Type:",row[3])
        file.close()

def donor_with_blood():
    blood_type = input("Blood type required:")
    Blood_types = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    if blood_type in Blood_types:
        with open("donors.txt", 'r') as file:
            donors = csv.reader(file)
            for row in donors:
                if blood_type == row[3]:
                    print("Name:",row[0]," Contact No:",row[1])
            file.close()
    else:
        print("Choose proper blood type.")
        donor_with_blood()

def donor_with_blood_help(blood_type):
    Blood_types = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    if blood_type in Blood_types:
        with open("donors.txt", 'r') as file:
            donors = csv.reader(file)
            for row in donors:
                if blood_type == row[3]:
                    print("Name:",row[0]," Contact No:",row[1])
            file.close()
    else:
        print("Choose proper blood type.")
        donor_with_blood()

def Add_donor():
    append_donor = open("donors.txt", 'a')
    name_ = name()
    contact_ = contact()
    blood_group = blood()
    date_ = date.today()
    append_donor.write(f"\n{name_},{contact_},{date_},{blood_group}")
    append_donor.close()

def Add_hospital():
    append_hospital = open("hospitals.txt",'a')
    _name = name()
    contact_ = contact()
    area = input("Area:")
    append_hospital.write(f"\n{_name},{contact_},{area}")
    append_hospital.close()

def View_hospital():
    with open("hospitals.txt", 'r') as file:
        donors = csv.reader(file)
        for row in donors:
            print("Name:",row[0],"Contact No:",row[1],"Area:",row[2])
        file.close()

