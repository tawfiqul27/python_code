# Working with os.path module

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print the name of the OS
    print(os.name)

    # check for item existence and type
    print("Item exists: " + str(path.exists("/home/islamam/Desktop/python_scripts/textfile.txt")))
    print("Item is a file: " + str(path.isfile("/home/islamam/Desktop/python_scripts/textfile.txt")))
    print("Item is a directory: " + str(path.isdir("/home/islamam/Desktop/python_scripts/textfile.txt")))


    # work with file paths
    print("Item path: " + str(path.realpath("/home/islamam/Desktop/python_scripts/textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("/home/islamam/Desktop/python_scripts/textfile.txt"))))


    # file modification time
    t = time.ctime(path.getmtime("/home/islamam/Desktop/python_scripts/textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("/home/islamam/Desktop/python_scripts/textfile.txt")))


    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("/home/islamam/Desktop/python_scripts/textfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + "seconds")



if __name__ == '__main__':
    main()
    














