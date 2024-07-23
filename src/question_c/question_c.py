#same initial code as q1

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol #private
        
        self.__company_name = company_name #private

    def get_symbol(self):
        return self.__symbol #returns symbol

    def get_company_name(self):
        return self.__company_name #returns company name

def stock_purchase_history(): #create function that creates 5 variables
    apple = Stock("AAPL", "Apple Inc.")
    caterpillar = Stock("CAT", "Caterpillar")
    eastman_kodak = Stock("EK", "Eastman Kodak")
    google = Stock("GOOG", "Google")
    microsoft = Stock("MSFT", "Microsoft")
    
    #create dictionary with all above items
    stock_dictionary = {apple.get_symbol(): apple,caterpillar.get_symbol(): caterpillar,eastman_kodak.get_symbol(): eastman_kodak,google.get_symbol(): google,microsoft.get_symbol(): microsoft}
    print("Symbol".ljust(5), "  Company")
    for symbol, stock in stock_dictionary.items():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(stock.get_symbol().ljust(5),"  ",stock.get_company_name().ljust(5))
        print("\n\n~~~See above history~~~\n\n...Rerouting to Main Menu...")
#############################################################################
def menu_all():
    print("\nFinal Menu\n-----------------------------------------------------")
    print("1- Display Stock Purchase History")
    print("2- Exit")
    
    user_option = input("Please select an option:\n")
    
    if user_option == "1":
        option_1()
    elif user_option == "2":
        option_2()
    else:
        print("\nPlease select a valid number input.")
        menu_all()

def option_1():
    stock_purchase_history()
    menu_all()

def option_2():
    print("\n...Program Exited...\n")