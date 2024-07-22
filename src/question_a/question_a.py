#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol#private
        
        self.__company_name = company_name#private

    def get_symbol(self):
        return self.__symbol#private to public via function

    def get_company_name(self):
        return self.__company_name#private to public via function