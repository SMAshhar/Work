###########################################################################################
################### Self registeration students on the University portal ##################
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

###########################################################################################
############################### Defining the login function ###############################
###########################################################################################

def login():

    # Conditioning for while loop. As long as check is 0, loop will keep running.
    check = 0

    while check == 0:

        # Login process will require username and password. Here we are taking enrollment 
        # number as username.
        username = input("\tPlease Enter your Enrol No.     :    ")
        password = input("\tPlease Enter your password      :    ")

        # Loading data from data.json file in the same folder. username and password will 
        # be checked against this data.
        with open("data.json") as j:
            dict_1 = json.load(j)

            # Unless the following two conditions are true, the loop will keep on asking for 
            # username and passowrd.
            if username in dict_1 and dict_1[username][0] == password:
                check = 1
                x = input("\tLogin successful. Please press enter to view your Student ID card : ")
                
                # The following template block will generate the students ID card putting in all 
                # the infromation from dict_1. 
                                   
                print(f"""       
                \t\t========================================================\t
                \t\tABC University for Computer Sceinces
                \t\t========================================================\t

                \t\tName = {dict_1[username][1]} {dict_1[username][2]}
                \t\tFather's Name = {dict_1[username][3]}
                \t\tCNIC = {dict_1[username][4]}
                \t\tCourse Applied = {dict_1[username][5]}
                \t\tEnroll. No = {username}

                \t\tPlease don't loose your assigned Enrollment number
                \t\t========================================================\t
                """)

            # If the two conditions from line 44 aren't true, it prompt the user to try again and 
            # will re-initiate the login sequence

            else:
                print("\tData doesn't match, Please try again.")

###########################################################################################
############################# Defining the register function ##############################
###########################################################################################

def register():

    # Loading data from data.json for checking against CNIC availability
    with open("data.json") as j:
        dict_1 = json.load(j)

    # Loading data from data.csv, which will be used to generate the new Enrollment Number
    with open("data.csv", "r") as f:
        x = csv.reader(f)
        y = []
        for a in x:
            y += a

    # A check for the loop which will run through the data from data.json file
    check = 0
 
    while check == 0:                  

        CNIC = input("\tPlease enter your CNIC : ")

        for a in dict_1.values():
            # check2 will be used to communicate the findings from the for loop for registeration check for further 
            # processing 
            check2 = 1
            if CNIC == a[4]:

                print("\tThis CNIC has already been registered. Please try again.")
                check2 = 0

            else:
                continue
        # If no match for current registered CNIC are found, check will be set to 1, thereby ending the while
        # loop and continuing on with the next step.    
        if check2 == 1:
            check = 1

###########################################################################################
############################### Starting program from here. ###############################
###########################################################################################       
    
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
#################################################
***

Welcome to ABC School online portal

***
#################################################
""")

choice = input("""#################################################

Please select your preference:

    Press 1 for Login
    Press 2 for New Registeration
    Choice : """)

if choice == "1":
    login()

elif choice == "2":
    register()

