# # reading and writing files

def main():
    #open a file for writing and create it if it doesn't exist
    f = open("/home/islamam/Desktop/python_scripts/textfile.txt", "w+")  # call the 'open' function. And it takes two arguments (1st is the file to operate on, the second argument is the kind of access that you want)
    # the plus sign is to cerate the file if it doesn't already exists


    # open the file for appending text to the end
    #c = open("/home/islamam/Desktop/python_scripts/appended_textfile.txt", "a")     # a parameter is for appending a text file
    c = open("/home/islamam/Desktop/python_scripts/appended_textfile.txt", "r")


    # write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")  # write function write data to the file. Then the file needs to be closed


    #for p in range(10):
    #    c.write("This is line " + str(p) + "\r\n")


    # close the file when done
    f.close()
    # c.close()


    # open the file back up and read the contents
    if c.mode == 'r':
        # contents = c.read()
        fl = c.readlines()
        for x in fl:
            print(x)
        # print(contents) 

    #

if __name__ == '__main__':
    main()
    

































