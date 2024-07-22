from question_a import Stock

Stock_List = [Stock("AAPL", "Apple Inc."),Stock("CAT", "Caterpillar"),Stock("EK", "Eastman Kodak"), Stock("GOOG", "Google"),Stock("MSFT", "Microsoft")]

for Stock in Stock_List:#magic
    print("Company Name: ", Stock.get_company_name(),"\n")#function that pull private data to public
    print("Symbol: ", Stock.get_symbol(),"\n-----------------------------")#function that pull private data to public