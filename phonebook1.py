import sys
def i_phonebook():
    rows,cols = int(input("please enter initial number of contacts: ")),5
    p_b = []
    print(p_b)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
    print("...................................................................................................................................")
    temp = []
    for j in range(cols):
        if j == 0:
            temp.append(str(input("Enter name*: ")))
            if temp[j == '' or temp[j] == ' ':]
            sys.exit("Name is a mandatory field. Prcess exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter number*: ")))
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter DOB(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter a category(Family/Friends/Work/Others): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        p_b.append(temp)
    print(p_b)
    return p_b
def menu():
    print("***********************************************************************************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("***********************************************************************************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact.")
    print("2. Remove an existing contact.")
    print("3. Delete all contacts.")
    print("4. Search for a contact.")
    print("5. Display all contacts.")
    print("6. Exit phonebook.")
    choice = int(input("Please enter your choice: "))
    return choice