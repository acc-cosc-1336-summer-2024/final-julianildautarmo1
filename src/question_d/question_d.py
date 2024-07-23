#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []
    for x in range(1,6):
        row = []
        for y in range(1,11):
            row.append(x*y)
        table.append(row)

    return table

def display_multiplication_table(list):
    z = create_multiplication_table()

    for row in z:
        for num in row:
            print(num, end="\t")
        print("\n")
##########################################################################################################
def menu():
    print("\nDo you want to keep going?\n-----------------------------------------------------")
    print("1- Yes")
    print("2- No")
    
    user_option = input("Please select an option:\n")
    
    if user_option == "1":
        option_1()
    elif user_option == "2":
        option_2()
    else:
        print("\nPlease select a valid number input.")
        menu()

def option_1():
    x = 0
    create_multiplication_table() == x

    display_multiplication_table(x)
    
    print("Rebooting...")
    menu()

def option_2():
    print("\n...Program Exited...\n")