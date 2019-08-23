# print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n Up above the world so high, \n\tLike a diamond in the sky. \nTwinkle, twinkle, little star, How I wonder what you are!")



# Write a Python program to get the Python version you are using.
# import sys

# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)
# print(sys.api_version)

#Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print(now)
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


# Write a Python program which accepts the radius of a circle from the user and compute the area.

# from math import pi
# r = float(input('Enter the radius of the circle: '))
# print("Area of the circle with radius "+ str(r)+" is: "+ str(pi * r**2))



# f_extns = ['big','json']
# print ("The extension of the file is : {}".format(f_extns[-1]))     #same as  print ("The extension of the file is : " + repr(f_extns[-1]))


# Write a Python program to print the calendar of a given month and year.

# import calendar
# y = int(input("Input the year : "))         # 2017
# m = int(input("Input the month : "))        # 04
# print(calendar.month(y, m))

# from datetime import date
# f_date = date(2013, 8, 21)
# l_date = date(2019, 5, 1)
# delta = l_date - f_date
# print(delta.days)


# Write a Python program to create a histogram from a given list of integers.

# def histogram(n):
#     for i in n:
#         print('@'*i)
#     return n

# histogram([2,3,6,5])
#print(b)        # if you print, return arg will take place and return will print at the end. If you don't print return value will not print



# Write a Python program to check whether a file exists.
# import os.path
# # open('/home/islamam/Desktop/python_scripts/abc.txt')
# print(os.path.isfile('abc.txt'))


# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS?
# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)


# Write a Python program to get OS name, platform and release information.
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())


# Write a Python program to locate Python site-packages.
# import site; 
# print(site.getsitepackages())


# Write a python program to call an external command in Python.
# from subprocess import call
# call(["ls","-l"])


# Write a python program to get the path and name of the file that is currently executing.
# import os
# print("Current File Name : ",os.path.realpath(__file__))


# Write a Python program to find out the number of CPUs using.
# import multiprocessing
# print(multiprocessing.cpu_count())


# Write a Python program to list all files in a directory in Python.
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/islamam') if isfile(join('/home/islamam', f))]
# print(files_list);


# Write a Python program to clear the screen or terminal.
# import os
# import time
# # for windows
# # os.system('cls')
# os.system("ls")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')



# Write a Python program to print the current call stack.
# import traceback
# print()
# # def f1():return abc()
# def abc():traceback.print_stack()
# # f1()
# abc()
# print()




# Write a Python program to check if a string is numeric.
# str = 'a123'
# str = '123'
# try:
#     i = float(str)
# except (ValueError, TypeError):
#     print('\nNot numeric')
# print()



# Write a Python program to convert a byte string to a list of integers.

# x = b'Abc'
# print(x)
# print(list(x))
# print()



# Write a Python program to get the details of sys module.
# import sys
# print(dir(sys))



# Write a Python program to sort files by date.
# import glob
# import os

# files = glob.glob("*.txt")
# print(files)
# files.sort(key=os.path.getmtime)
# print("\n".join(files))



#  Write a Python program to determine profiling of Python programs.

# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
# These statistics can be formatted into reports via the pstats module.

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')


# Write a Python program to get the users environment.
# import os
# print()
# print(os.environ)
# print()


# Write a Python program to extract the filename from a given path.
# import os
# print()
# print(os.path.basename('/home/islamam/Desktop/python_scripts/Practice problem/practice_033.py'))
# print()


# Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
# import os
# print("\nEffective group id: ",os.getegid())
# print("Effective user id: ",os.geteuid())
# print("Real group id: ",os.getgid())
# print("List of supplemental group ids: ",os.getgroups())
# print()


# 113 Write a Python program to input a number, if it is not a number generate an error message.

# try:
#     a = int(input('Enter a number: '))

# except ValueError:
#     print('This is not a number. Try a number....')



# from collections import deque

# q = deque(["buffy", "xander", "willow"])
# q.append("giles")

# print(q)

# q.rotate(2)

# print(q)

# def fib(i):
#     if i < 2: return 1
#     return fib(i-1) + fib(i-2)


# x = fib(13)
# print(x)


#============================ merge two lists
# num = input ("Enter number :") 
# print(num) 
# print(num, end=" ")

list = [1,2,4,5,6,7,8]
list1 = [10,9,13,3,6,11]

s = [str(i) for i in list]  # change the comma seperated list to string
print(s)                    # 
l = " ".join(s)
print(l)           # this will join a string to make single string
 
k = l.split(' ')    # this convert string to list 
print(k)


list3 = (list + list1)
p = sorted(list3)       # sorted must be used to save the output to a variable 
print(p)
print(max(p))           # to print the largest value in a list   
print(min(p))           # to print the smallest value in the list       
print(sum(p))           # print the sum
print(p.index(11))      # print the index of 11 in list3



# OR, but it is throwing error. So, for now try to follow the first one

# from heapq import merge
# test_list1 = [1, 5, 6, 9, 11] 
# test_list2 = [3, 4, 7, 8, 10] 
# print ("The original list 1 is : " + str(test_list1)) 
# print ("The original list 2 is : " + str(test_list2)) 
# res = list(merge(test_list1, test_list2)) 
# print ("The combined sorted list is : " + str(res)) 





