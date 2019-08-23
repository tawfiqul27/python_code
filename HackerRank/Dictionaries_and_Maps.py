# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then 
# be given an unknown number of names to query your phone book for. For each 'name' queried, print the associated entry from your phone 
# book on a new line in the form name=phoneNumber; if an entry for 'name' is not found, print 'Not found' instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Input Format
# The first line contains an integer,n , denoting the number of entries in the phone book. Each of the n subsequent lines describes 
# an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 
# 8-digit phone number.

# After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a 'name' to look up, 
# and you must continue reading lines until there is no more input.
# Note: Names consist of lowercase English alphabetic letters and are first names only.

# Constraints
# 1<=n<=10^5
# 1<=queries<=10^5

# Output Format

# On a new line for each query, print 'Not found' if the name has no corresponding entry in the phone book; otherwise, print the full 'name'
#  and 'phone Number' in the format name=phoneNumber.


# Sample Input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

# Sample Output:
# sam=99912222
# Not found
# harry=12299933

#===========================================
# Learning: 
# Taking multiple inputs from user in Python-    input().split(separator, maxsplit)

# # taking two inputs at a time 
# x, y = input("Enter a two value: ").split() 
# print("Number of boys: ", x) 
# print("Number of girls: ", y) 
# print() 

# # taking three inputs at a time 
# x, y, z = input("Enter a three value: ").split() 
# print("Total number of students: ", x) 
# print("Number of boys is : ", y) 
# print("Number of girls is : ", z) 
# print() 

# Output:
# Enter a two value: 5 10
# Number of boys: 5
# Number of girls: 10

# Enter a three value: 30 10 20
# Total number of students: 30
# Number of boys is: 10
# Number of girls is: 20
#============================================ my solution 
import sys

n = int(input())
if 0<=n<=10^5:
    phonebook = {}
    for i in range(0,n):
        x,y= input().split()
        phonebook[x]= y 
lines = sys.stdin.readlines()       # this will take all the inputs from user and executes rest of the lines at once. Ctrl+d to stop adding input
for queries in lines:
    name = queries.strip()
    if name in phonebook.keys():
        print(name+ "=" + phonebook[name])
    else:
        print("Not found")




#======================================= solution from hackerrank
# import sys 

# # Read input and assemble Phone Book
# n = int(input())
# phoneBook = {}
# for i in range(n):
#     contact = input().split(' ')
#     phoneBook[contact[0]] = contact[1]

# # Process Queries
# lines = sys.stdin.readlines()
# for i in lines:
#     name = i.strip()
#     if name in phoneBook:
#         print(name + '=' + str( phoneBook[name] ))
#     else:
#         print('Not found')




