# Working with date information

# these below command will tell python interpreter that from the datetime interpreter module that comes with the standard library
# I want to import the date, time, and datetime classes. These are predifined pieces of functionality in the pyhton library that let me manipulate dates and times
# To use these functions, we need to import it.


from datetime import date
from datetime import time
from datetime import datetime

def main():
    # Date objects
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date components; ", today.day, today.month, today.year)


    # Retrive today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday number: ", today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("Which is a: ", days[today.weekday()])
    

    ## DATETIME Objects
    # Get today's date from the datetime class
    currentday = datetime.now()
    print("The current date and time is: ", currentday)
    
    # Get the current time
    t = datetime.time(datetime.now())
    print(t)

if __name__ == '__main__':
   main()
    














