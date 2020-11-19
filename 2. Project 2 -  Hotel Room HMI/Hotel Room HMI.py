###########################################################################################
############################## Hotel Room Console HMI Software ############################
###########################################################################################
### This program will do the following:                                                 ###
### 1. Ask user for room no as user and a pre-generated key given during checking in.   ###
### 2. Load data from the data file.                                                    ###
### 3. check if details match, if match, go ahead, if not, return to step i             ###
### 4. If go ahead, Prompt user of success.                                             ###
### 5. Ask to choose to Order Food or add a complaint.                                  ###
### 6. If complaint is selected, following path is followed.                            ###
###     i,      Display pre-made menu card.                                             ###
###     ii,     Take input for ordering.                                                ###
###     iii,    Store the order in a list                                               ###
###     iv,     Ask if continue or keep adding more items.                              ###
###     v,      If keep adding more items, move to point (i).                           ###
###     vi,     Else, ask if want to quite or stay logged in.                           ###
###     vii,    If stay logged in, return to point(5), else, end program with a message.###
### 3. If complaint route is choosen, it will go down the following path:               ###
###     i,      Display predefined catagories of complaints.                            ###
###     ii,     Input: Ask user to select one.                                          ###
###     iii,    Input: Ask user to enter message.                                       ###
###     iv,     Assign the compaint a number and display it to user for later reference.###
###     v,      Store complaint in a file named by complaint number for later use.      ###
###     vi,     Generate a thank you message.                                           ###
###     vii,    Ask the user if he wants to continue. If yes, go to point(5).           ###
###     viii,   Else end program with a message.                                        ###
###########################################################################################
###########################################################################################

import datetime
import json

# We have defined floors of the hotel, each having 4 rooms. 
# Each room is assigned a separate 4-digit key which will be provided to current owner.
# These will be used by user to login to the HMI provided in the hotel room.

dict1 = {"A1" : 8567,
         "A2" : 6741,
         "A3" : 7845,
         "A4" : 2587,
         "B1" : 6541,
         "B2" : 9875,
         "B3" : 8546,
         "B4" : 9673,}

###########################################################################################
############################### Defining the login function ###############################
###########################################################################################

def login():

    # This print section will be displayed defining the successful transition to the login path

    print("""
                
    ****************************************
                
        Welcome to the ABC Hotel Service.
                
    ****************************************
                
    """)
    # The username will be used through out the session as in several locations. Defining it 
    # as global was necessary.
    global username 

    chance = 1
    while chance == 1:
        
        username = input("\tPlease Enter your Room Number  : ")
        password = int(input("\tPlease Enter your 4-digit key  : "))

        # Checking for correct data
        for a in dict1.keys():
            if a == username and dict1[username] == password:
                print("-------------------------------------------------------------------")
                print("\tLogin Successful.")
                print("-------------------------------------------------------------------")
                chance = 0
                # The choice function will be called from inside the login function.
                choice()
                break

        if chance == 1:
            print("\tNo match found. Please try again.")
            print("-------------------------------------------------------------------")

###########################################################################################
###################### Defining the Food/Complain Choice function #########################
###########################################################################################

def choice():
    print("-------------------------------------------------------------------")
    print("""        Welcome to ABC Hotel's Online Service               """)
    print("-------------------------------------------------------------------")
    x = input("""
        Please select from following menu: 
            1. Enter 1 for ordering of food
            2. Enter 2 for listing a complain
            Choice : """)
    if x == "1":
        # If choice 1 is selected, the food function will be called from inside the 
        # choice function. 
        print("-------------------------------------------------------------------")
        food()

    elif x == "2":
        # If choice 2 is selected, the complain function will be called from inside the 
        # choice function.
        print("-------------------------------------------------------------------")
        complain()

    else:
        # If wrong input is entered, it will recall the choice function, prompting user
        # of the mistake
        print("\tWrong Input. Please try again.")
        print("-------------------------------------------------------------------")
        
        choice()
    

###########################################################################################
############################### Defining the Food function ################################
###########################################################################################

###########################################################################################
### The food function will do the following jobs:                                       ###
### 1. Identify what time of the day is it from morning, afternoon and eavening.        ###
### 2. Load data from pre-designed menu for that perticular time                        ###
### 3. Display the the appropriate menu.                                                ###
### 4. Take input from user about what does they want. Do repeat if they input          ###
### something wrong.                                                                    ###
### 5. Take selection, compile the selection and generate a .txt file with the room     ##
### name and order detail.                                                              ###        
###########################################################################################

def food():
    # Identifying current datetime via datetime module
    now = datetime.datetime.now()

    #  Checking if it is breakfast time. 
    if now < now.replace(hour=11, minute=0, second=0, microsecond=0):
        # loading data for breakfast
        with open("breakfast.json") as j:
            menu = json.load(j)

        # Prompting user for selction of choice
        print("\tPlease select from the following menu : ")

        # Printing all the choices one-by-one
        for a in menu.keys():
            print(f"\t{a} : {menu[a][0]} : {menu[a][1]}")
        
        # Taking input for user selection.
        print("-------------------------------------------------------------------")
        foods = input("\tChoice : ")
        print("-------------------------------------------------------------------")
        # If bad selection is made, food function will be called again with a prompt
        # to the user.
        if foods not in menu.keys():
            print("\tPlease select from the provided list")
            print("-------------------------------------------------------------------")
            food()
        # If selection is within bounds, function will continue.
        else:
            order = f"""        {menu[foods][0]} breakfast selected. Please wait, your 
        breakfast will be at your door in a few minutes."""
            print(order)
            # The order will be placed in a .txt file named against the room number, 
            # carrying details about the order.
            with open((username+".txt"), "w") as f:
                f.write(f"{username} : {menu[foods]}")

    # Checking if it is lunch time.

    elif now < now.replace(hour=17, minute=0, second=0, microsecond=0):
        # loading data for lunch
        with open("lunch.json") as j:
            menu = json.load(j)

        # Prompting user for selction of choice
        print("\tPlease select from the following menu : ")

        for a in menu.keys():
            print(f"\t{a} : {menu[a][0]} : {menu[a][1]}")
        print("-------------------------------------------------------------------")
        foods = input("\tChoice : ")
        print("-------------------------------------------------------------------")
        # If bad selection is made, food function will be called again with a prompt
        # to the user.
        if foods not in menu.keys():
            print("\tPlease select from the provided list")
            print("-------------------------------------------------------------------")
            food()

        else:
            order = f"""        {menu[foods][0]} lunch selected. Please wait, 
        your lunch will be at your door in a few minutes."""
            print(order)
            # The order will be placed in a .txt file named against the room number, 
            # carrying details about the order.
            with open((username+".txt"), "w") as f:
                f.write(f"{username} : {menu[foods]}")
        

    # Checking if it is lunch time.

    elif now < now.replace(hour=23, minute=0, second=0, microsecond=0):
        # loading data for dinner
        with open("dinner.json") as j:
            menu = json.load(j)

        print("\tPlease select from the following menu : ")

        for a in menu.keys():
            print(f"\t{a} : {menu[a][0]} : {menu[a][1]}")
        print("-------------------------------------------------------------------")

        foods = input("\tChoice : ")
        print("-------------------------------------------------------------------")
        # If bad selection is made, food function will be called again with a prompt
        # to the user.
        if foods not in menu.keys():
            print("\tPlease select from the provided list")
            print("-------------------------------------------------------------------")
            food()

        else:
            order = f"""        {menu[foods][0]} dinner selected. Please wait, 
        your dinner will be at your door in a few minutes."""
            print(order)
            # The order will be placed in a .txt file named against the room number, 
            # carrying details about the order.
            with open((username+".txt"), "w") as f:
                f.write(f"{username} : {menu[foods]}")
    print("-------------------------------------------------------------------")

    input()
    # Recalling the choice function takes you to back to the welcome screen.
    choice()

###########################################################################################
############################# Defining the Complain function ##############################
###########################################################################################

def complain():

    # Datetime is identified here as a stamp on the complaint.
    now = datetime.datetime.now()

    # Catagory will be predefined as "Others", will change with future choice.
    Catagory = "Others"

    print("""
        FIrst of all, we highly regret that you have to come to this section.
        Please select from the following catagories : 
        """)
    catagories = ["Staff", "Food", "Room", "Room Service", "Security"]

    # Listing the catagories in a list manner.
    for i, item in enumerate(catagories):
        print("\t", i+1, item)

    # Innitiating error handling. If a catagory was selected from one of the 
    # listed ones, it will change the catagory to that. Else, catagory will
    # remain "Others".
    try:
        complainType = int(input("""
        Please enter from 1 to 5 to select catagory, else press any key for 
        others catagory : """))
        if complainType > 0 and complainType <= 5:
            Catagory = catagories[complainType - 1]
    # If user chooses something else, the function continues with catagory as
    # "Others".
    except:
        pass
    
    complain = input("""
        Please enter the detail of your complain below the line: 
        --------------------------------------------------------
        """)
    print("-------------------------------------------------------------------")
    complain = f"{Catagory} : {complain}"
    print("\t", complain, sep=(""))


    b = ""
    x = str(now)
    for a in x:
        if a != "-" and a != ":":
            b += a

    with open((f"{username} {b[:15]}.txt"), "w") as f:
        f.write(complain)

    print("\tYour complain has been registered.")
    print("-------------------------------------------------------------------")

    input()

    choice()


login()
            


        

       