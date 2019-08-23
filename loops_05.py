# Working with loops
#

def main():
    x = 0
    
    
    # define a while loop
    while (x<5):
        print(x)
        x = x+1

    print("This is the break between while and for loop")
    
    
    # define a for loop
    for x in range(5, 10):
        print(x)


    print ("This is the break between two different type of for loops")
    # use a for loop over a collection
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)


    print("This for loop is the use of break and continue statement")
    
    
    # use the break and continuous statements
    for x in range(5,10):
        # if (x==8): break
        if (x<=7): continue
        print(x)


    print("This is the beginning of enumeration")

    # using the enumerate() function to get index
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):     # this will print the index along with the value
        print(i, d)

if __name__ == '__main__':
    main()
        