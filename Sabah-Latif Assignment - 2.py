###########################################################################################
##################### Self registeration students on the school website ###################
###########################################################################################
### This program will do the following:                                                 ###
### 1. Ask user for a login path or a registeration path                                ###
### 2. If login is chosen, it will go down the following path:                          ###
###     i,      Input details (enroll. no., password)                                   ###
###     ii,     Load data from the data file                                            ###
###     iii,    check if details match, if match, go ahead, if not, return to step i    ###
###     iv,     if go ahead, message to the user for successful login and print card.   ###
###     v,      exit                                                                    ###
### 3. If registeration is choosen, it will go down the following path:                 ###
###     i,      Input details (CNIC)                                                    ###
###     ii,     If CNIC not registered, go ahead, else return to step 1                 ###
###     iii,    Input further details (name, father's name, course etc)                 ###
###     iv,     Generate enrollment no.                                                 ###
###     v,      Store data for later use.                                               ###
###     vi,     Generaet student card                                                   ###
###     vii,    Display student ID card                                                 ###
###     viii,   Exit                                                                    ###
###########################################################################################
###########################################################################################

import json
import csv

def login():

    check = 0

    while check == 0:

        username = input("\tPlease Enter your Enrol No.     : ")
        password = input("\tPlease Enter your password      : ")

        with open("data.json") as j:
            dict_1 = json.load(j)

            if username in dict_1 and dict_1[username][0] == password:
                check = 1
                x = input("\tLogin successful. Please press enter to view your Student ID card : ")
                
                                    
                print(f"""       
                \t\t========================================================\t
                \t\tABC University for Computer Sceinces
                \t\t========================================================\t

                \t\tName = {dict_1[username][1]} {dict_1[username][2]}
                \t\tFather's Name = {dict_1[username][3]}
                \t\tCNIC = {dict_1[username][4]}
                \t\tCourse Applied = {dict_1[username][5]}
                \t\tR. No = {username}

                \t\tPlease don't loose your assigned Enrollment number
                \t\t========================================================\t
                """)
            else:
                print("\tData doesn't match, Please try again.")


def register():

    with open("data.json") as j:
        dict_1 = json.load(j)

    with open("data.csv", "r") as f:
        x = csv.reader(f)
        y = []
        for a in x:
            y += a

    check = 0
    check2 = 0
    
    while check == 0:                  

        CNIC = input("\tPlease enter your CNIC : ")

        for a in dict_1.values():
            check2 = 1
            if CNIC == a[4]:
                print("\tThis CNIC has already been registered. Please try again.")
                check2 = 0
            else:
                continue
        if check2 == 1:
            check = 1

            
    print("\tCNIC available.")

    print("""
                
    *****
                
    Welcome to the registeration section.
                
    *****
                
    """)

    firstName = input("\tPlease Enter your First name : ")
    lastName = input("\tPlease enter your last name : ")
    fatherName = input("\tPlease enter your Father's name : ")
    course = input("\tPlease enter the applied course : ")
    password = input("\tPlease enter password for your profile : ")

    enroll = course[:2] + str(int(y[-1][-4:]) + 1)
                

    dict_1[enroll] = [password, firstName, lastName, fatherName, CNIC, course]
    print(dict_1)
    y = [enroll]
                
    print(enroll)

    with open("data.json", "w") as j:
        json.dump(dict_1, j)

    with open("data.csv", "a", newline = "") as f:
        z = csv.writer(f, delimiter = ",")
        z.writerow(y)

            
    print(f"""    
                \t\t========================================================\t
                \t\tABC University for Computer Sceinces
                \t\t========================================================\t

                \t\tName = {firstName} {lastName}
                \t\tFather's Name = {fatherName}
                \t\tCNIC = {CNIC}
                \t\tCourse Applied = {course}
                \t\tEnroll. No. = {enroll}

                \t\tPlease don't loose your assigned Enrollment number
                \t\t========================================================\t
                """)




print("""

***

Welcome to ABC School online portal

***

""")

choice = input("""

Please select your preference:

    Press 1 for Login
    Press 2 for New Registeration
    Choice : """)

if choice == "1":
    login()

elif choice == "2":
    register()

