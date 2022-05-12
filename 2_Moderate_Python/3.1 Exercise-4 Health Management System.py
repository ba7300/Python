"""
                   ###    Health Management System     ###

"""


from logging import exception


Client_List = {1:'Bhavik',2:'Dhiraj',3:'Viky',4:'Janmesh',5:'Shubham'}
Log_List = {1:'Exercise', 2:'Diet'}
Opr_List = {1:'Log', 2:'Retrieve'}


def gatedate():
    import datetime
    return datetime.datetime.now()

try:
    print("\n Select client name: \n")
    for key,value in Client_List.items():
        print(f"Enter {key} for {value} ")
    print('\n')

    C_name = int(input("Enter Client ID: "))
    print(f"Selected Client is {Client_List.get(C_name)}.")
    print(f"Welcome Mr.'{Client_List.get(C_name)}'. \n")

    print("Select the service you would like to access from below options:")
    for key,value in Opr_List.items():
        print(f"Enter {key} for {value}.")
    print('\n')
    Opr_name = int(input('Enter the operation: '))
    print(f"You have selected {Opr_List.get(Opr_name)} Operation.")
    print('\n')

    if Opr_name is 1:
        for key,value in Log_List.items():
            print(f"Enter {key} to create {value} Report")

        L_name = int(input("Enter Report ID: "))
        print(f"You have slected {Log_List.get(L_name)} Log")
        print('\n')

        with open(f"client_details/{Client_List.get(C_name)}_{Log_List.get(L_name)}.txt",'a') as f:

            Q = 'y'
            while Q is 'y':
                MyData = input(f"Enter {Log_List.get(L_name)} : ")
                f.write(f"[{str(gatedate())}] : {MyData}")

                Q = input(f"Do you want to Add more{Log_List.get(L_name)}? (Enter 'y' to Add / Enter 'n' to Close): ")
                continue
            print('Your Data has been updated successfully. I hope you are satisfied with our service.')


    elif Opr_name is 2:
        for key,value in Log_List.items():
            print(f"Enter {key} for {value} Report")

        L_name = int(input("Enter Log ID: "))
        print(f"Slected Log is {Log_List.get(L_name)}")
        print('\n')

        print(f"{Client_List.get(C_name)}_{Log_List.get(L_name)} Report: \n")
        
        with open(f"client_details/{Client_List.get(C_name)}_{Log_List.get(L_name)}.txt") as f:
            contents = f.readlines()
            for line in contents:
                print(line,end='')

    else:
        print("Invalid Input !!! \n Please Enter Right Value.")


except exception as e:
    print("Wrong Input !!!")