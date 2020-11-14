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
###     ii,     If email address available, go ahead, else return to step 1             ###
###     iii,    Input further details (name, father's name, department)                 ###
###     iv,     Generate enrollment no.                                                 ###
###     v,      Store data for later use.                                               ###
###     vi,     Generaet student card                                                   ###
###     vii,    Display student ID card                                                 ###
###     viii,   Exit                                                                    ###
###########################################################################################
###########################################################################################

import json

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

