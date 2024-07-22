#write functions here, don't add input('') statements here!

num_list = []

def add_to_list():
    
    for i in range(5):
        num = int(input("Enter a whole #. "))#i know it says not to put input() here but this lets me put it directly into the loop and makes it all cleaner
        num_list.append(num)#add to end of list
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return num_list

def show_list_data():
    print("The lowest of your 5 #'s is: ", min(num_list))#min fo list
    print("The highest of your 5 #'s is: ", max(num_list))#max of list
    print("The total of your 5 #'s is: ", sum(num_list))#net total
    print("The average of your 5 #'s is: ", sum(num_list)/len(num_list)) #sum/amount


