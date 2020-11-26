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
###     v,      Recall 1.                                                               ###
### 3. If registeration is choosen, it will go down the following path:                 ###
###     i,      Input details (CNIC)                                                    ###
###     ii,     If CNIC not registered, go ahead, else return to step 1                 ###
###     iii,    Input further details (name, father's name, course etc)                 ###
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

    if choice == "1":
        login()

    elif choice == "2":
        register()




            # Unless the following two conditions are true, the loop will keep on asking for 
            # username and passowrd.
            if username in dict_1 and dict_1[username][0] == password:
                check = 1
                x = input("\tLogin successful. Please press enter to view your Student ID card : ")
                
                # The following template block will generate the students ID card putting in all 
                # the infromation from dict_1. 
                                   
                print(f"""       
                \t\t========================================================\t
                \t\t        ABC University for Computer Sceinces
                \t\t========================================================\t
                                    \t\t STUDENT ID CARD

                \t\tName = {dict_1[username][1]} {dict_1[username][2]}
                \t\tFather's Name = {dict_1[username][3]}
                \t\tCNIC = {dict_1[username][4]}
                \t\tCourse Applied = {dict_1[username][5]}
                \t\tEnroll. No = {username}

                \t\tPlease don't loose your assigned Enrollment number
                \t\t========================================================\t
                """)

            # If the two conditions from line 44 aren't true, it prompt the user to try again and 
            # will re-initiate the login sequence.

            else:
                print("\tData doesn't match, Please try again.")

    # This will bring back the initial page for path selection.
    welcome()

###########################################################################################
############################# Defining the register function ##############################
###########################################################################################

def register():

    # Loading data from data.js
            # check for further processing. 
            check2 = 1
            if CNIC == a[4]:

                print("\tThis CNIC has already been registered. Please try again.")
                check2 = 0

            else:
                continue
        # If no match for current registered CNIC are found, check will be set to 1, thereby ending 
        # the while loop and continuing on with the next step.    
        if check2 == 1:
            check = 1

    # Will print this line after the While loop dies. It will only happen if CNIC number provided has
    # never been used before.
    print("\tCNIC available.")

    # This print section will be display the successful transition from CNIC checkup to further data
    # collection.
    print("""
                
    *************************************
                
    Welcome to the registeration section.
                
    *************************************
                
    """)

    # From here,e CSV file, we need to convert the new generated enrollment number 
    # into list. Which is done below.
    y = [enroll]
 
    # The updated dict_1 is written on the json file.
    with open("data.json", "w") as j:
        json.dump(dict_1, j)

    # The CSV file is updated with the new enrollment number.
    with open("data.csv", "a", newline = "") as f:
        z = csv.writer(f, delimiter = ",")
        z.writerow(y)

    # After all the data is stored, the Student ID card is generated in the following format.     
    print(f"""    
                \t\t========================================================\t
                \t\t        ABC University for Computer Sceinces
                \t\t========================================================\t
                                    \t\t STUDENT ID CARD

                \t\tName = {
###########################################################################################
############################### Starting program from here. ###############################
###########################################################################################  

# The program will start with the following set of strings. 
print("""
#################################################
*************************************************

      Welcome to ABC School online portal

*************************************************
#################################################
""")

welcome()

