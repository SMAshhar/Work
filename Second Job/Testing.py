import json
import csv

def register():

    check = 0

    while check == 0:

        with open("data.json") as j:
            dict_1 = json.load(j)

        with open("data.csv", "r") as f:
            x = csv.reader(f)
            y = []
            for a in x:
                y += a
            
            print(y)
            
        CNIC = input("\tPlease enter your CNIC : ")

        for a in dict_1.values():
            if CNIC == a[4]:
                print("\tThis CNIC has already been registered. Please try again.")

            else:
                check = 1
                print("\tCNIC available.")

                print("""
                
                *****
                
                Welcome to the registeration section.
                
                *****
                
                """)

                firstName = input("\tPlease Enter your First name : ")
                secondName = input("\tPlease enter your last name : ")
                fatherName = input("\tPlease enter your Father's name : ")
                course = input("\tPlease enter the applied course : ")
                password = input("\tPlease enter password for your profile : ")

                enroll = course[:2] + str(int(y[-2][-4:-1]) + 1)
                y += enroll

                dict_1[enroll] = [password, firstName, secondName, fatherName, CNIC, course]
                print(dict_1)

                with open("data.json", "w") as j:
                    json.dump(dict_1, j)

                with open("data.csv", "w", newline = "") as f:
                    z = csv.writer(f, delimiter = ",")
                    z.writerow(y)

                break


register()

            # if username in dict_1 and dict_1[username][0] == password:
            #     check = 1
            #     print("\tLogin successful. Please press enter to view your Student ID card ")
            #     x = input("\t\t : ")
                                    
            #     print(f"""                        
            #     \t\tName = {dict_1[username][1]} {dict_1[username][2]}
            #     \t\tFather's Name = {dict_1[username][3]}
            #     \t\tCNIC = {dict_1[username][4]}
            #     \t\tCourse Applied = {dict_1[username][5]}
            #     \t\tR. No = {username}

            #     \t\tPlease don't loose your assigned Enrollment number
            #     \t\t========================================================\t
            #     """)
            # else:
            #     print("\tData doesn't match, Please try again.")

