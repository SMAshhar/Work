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
#
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
        
        choic
            menu = json.load(j)

        # Prompting user for selection of choice
        print("\tPlease select from the following menu : ")

        # Printing all the choices one-by-one
        for a in menu.keys():
            print(f"\t{a} : {menu[a][0]} : {menu[a][1]}")
        
        # Taking input for user selection.
        print("-------------------------------------------------------------------")
        foods = input("\tChoice : ")
        print("-------------------------------------------------------------------")
        # If bad selection is made, food function will be called again with a prompt
]} lunch selected. Please wait, 
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
##############################################

# The program will start as soon as we call the login function.

login()
