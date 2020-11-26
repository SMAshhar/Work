###########################################################################################
################### Self registeration students on the University portal ##################
###########################################################################################
### This program will do the following:                                                 ###
### 1. Ask user for a login path or a registeration path                                ###
### 2. If login is chosen, it will go down the following path:                          ###
###     i,      Input details (enroll. no., password)                                   ###
###     ii,     Load data from the data file                                            ###
###     iii,    check if details match, if match, go ahead, if not, return to step i    ###
###     iv,     If go ahead, Prompt user of success.                                    ###
###     v,      Ask to choose to print ID card or change password.                      ###
###     vi,     If print ID is selected, ID card is printed.                            ###
###     vii,    If change password is selected. Password changer function is called.    ###
###     viii,   Recall 1.                                                               ###
### 3. If registeration is choosen, it will go down the following path:                 ###
###     i,      Input details (CNIC)                                                    ###
###     ii,     If CNIC not registered, go ahead, else return to step 1                 ###
###     iii,    If go ahead, Input further details (name, father's name, course etc)    ###
###     iv,     Generate enrollment no.                                                 ###
###     v,      Store data for later use.                                               ###
###     vi,     Generate student ID card                                                ###
###     vii,    Display student ID card                                                 ###
###     viii,   Recall 1.                                                               ###
###########################################################################################
###########################################################################################

import json
import csv

###########################################################################################
############################# Defining the welcome function ###############################
###########################################################################################

def welcome():
    # User will choose the path to choose from the following statement. 
    choice = input("""#################################################

        Please select your preference:

        Press 1 for Login
        Press 2 for New Registeration
        Choice : """)

    # If choice is 1, login function is called. 
    if choice == "1":
        print("----------------------------------------------------")
        login() 

    # If choice is 2, register function is called.
    elif choice == "2":
        print("----------------------------------------------------")
        register()
        

    # If choice is any other, a prompt will be made for a proper selection.
    else:
        print("\n\tInvalid selection. Please try again.")
        print("----------------------------------------------------")
        input()
        welcome()


###########################################################################################
############################### Defining the login function ###############################
###########################################################################################

def login():

    # This print section will be displayed defining the successful transition to the login path

    print("""
                
    *************************************
                
        Welcome to the Login section.
                
    *************************************
                
    """)
8

            # Unless the following two conditions are true, the loop will keep on asking for 
            # correct username and password.
            if username in dict_1 and dict_1[username][0] == password:
                check = 1
                x = input("""

        Login successful. 
        Please:
        1. Enter 1 to view your Student ID card
        2. Enter 2 to change your current password 
        Choice : """)
        

                
                # The following template block will generate the students ID card putting in all 
                # the information from dict_1. 

                if x == "1": 
                    print("----------------------------------------------------")                 
                    print(f"""       
                    \t========================================================\t
                    \t        ABC University for Computer Sciences
                    \t========================================================\t
                                        \t\t STUDENT ID CARD

                    \tName = {dict_1[username][1]} {dict_1[username][2]}
                    \tFather's Name = {dict_1[username][3]}
                    \tCNIC = {dict_1[username][4]}

                print("\tData doesn't match, Please try again.")
                print("----------------------------------------------------")

    # This will bring back the initial page for path selection.
    input()
    welcome()

###########################################################################################
############################# Defining the register function ##############################
###########################################################################################

def register():

    # Loading data from data.json for checking against CNIC availability.
    with open("data.json") as j:
        dict_1 = json.load(j)

    # Loading data from data.csv, which will be used to generate the new Enrollment Number.
    with open("data.csv", "r") as f:
        x = csv.reader(f)
        y = []
        for a in x:
            y += a

    # A check for the loop which will run through the data from data.json file.
    check = 0
 
    while check == 0:                  

        CNIC = input("\tPlease enter your CNIC : ")
        print("----------------------------------------------------")

        for a in dict_1.values():
            # check2 will be used to communicate the findings from the for loop for registeration 
            # check for further processing. 
            check2 = 1
            if CNIC == a[4]:

                print("\tThis CNIC has already been registered. Please try again.")
                print("----------------------------------------------------")
                check2 = 0

            else:

                
    *************************************
                
    Welcome to the registration section.
                
    *************************************
                
    """)
    print("----------------------------------------------------")

    # From here, the data collection will start. Each input will be assigned to a variable for later
    # use in Student ID card generation.

    firstName = input("\tPlease Enter your First name : ")
    lastName = input("\tPlease enter your last name : ")
    fatherName = input("\tPlease enter your Father's name : ")
    course = input("\tPlease enter the applied course : ")
    password = input("\tPlease enter password for your profile : ")
    print("----------------------------------------------------")

    #########################################################################################################
    # Enrollment Number is generated in the following single statement. The statement is divided into two   #
    # parts. The "course[:2]" will take the first two charactors from the course input. i.e. if course is   #
    # CS50 the first part will be CS. In the same manner, if the course selection is EN30, the first part   #
    # will be EN. The next part (which is numeric part) is int(y[-1][-4:]) + 1. y[-1] represents the last   #
    # item from the data collected from the CSV file, and [-4:] represents the last 4 numbers from that     #
    # number. 1 is added in them to generate a new enrollment number.                                       #
    # Lastly, this number will be converted into string and added into the characters from the first        #
    # part. and the sum will generate a full enrollment number, for example: "CS" + "1234" = "CS1234"       #
    #########################################################################################################

    enroll = course[:2] + str(int(y[-1][-4:]) + 1)
                
    # dict_1 was taken from data.json. The dict_1 is updated with the new enrollment number. All data is 
    # stored as a list against the key, that is the new enrollment number. CNIC is taken from the approved
    # CNIC in line 157
    dict_1[enroll] = [password, firstName, lastName, fatherName, CNIC, course]

    # To add the enrollment number on the CSV file, we need to convert the new generated enrollment number 
    # into list. Which is done below.

    # Following statement is asking for user to input new password and is going to assign that
    # password to the provided username from login function.
    print("----------------------------------------------------")
    dict_2[username][0] = input("\tPlease enter your new password : ")
    print("----------------------------------------------------")

    # Once dict_2 is updated with a changed password, the updated change will be updated 
    # in the json file
    with open("data.json", "w") as j:
        json.dump(dict_2, j)

    # Prompting user for successful change.
    print("\tPassword has been successfully changed")
    print("----------------------------------------------------")
    input()

    # Program will continue on with the login function.
    
###########################################################################################
############################### Starting program from here. ###############################
###########################################################################################  

# The program will start with the following set of strings. 

print("""
#################################################
*************************************************

    Welcome to ABC University online portal

*************************************************
#################################################
""")

# From here, the welcome function is called. Thereby actually starting the program.
input()
welcome()
