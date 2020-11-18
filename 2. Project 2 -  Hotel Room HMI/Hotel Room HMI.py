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