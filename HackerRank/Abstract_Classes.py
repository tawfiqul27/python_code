# Task
# Given a Book class and a Solution class, write a MyBook class that does the following:
# - Inherits from Book
# - Has a parameterized constructor taking these parameters:
#         1. string title
#         2. string author
#         3. int price
# - Implements the Book class' abstract display() method so it prints these lines:
#         1. Title:, a space, and then the current instance's title.
#         2. Author:, a space, and then the current instance's author.
#         3. Price:, a space, and then the current instance's price.
# Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring 
# MyBook or your code will not execute.

# Input Format
# You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class 
# constructor (passing it the necessary arguments). It then calls the display method on the Book object.

# Output Format
# The void display() method should print and label the respective title, author, and price of the MyBook object's instance (with each 
# value on its own line) like so:
# Title: $title
# Author: $author
# Price: $price

# Note: The $ is prepended to variable names to indicate they are placeholders for variables.

# Sample Input: The following input from stdin is handled by the locked stub code in your editor:
# The Alchemist
# Paulo Coelho
# 248

# Sample Output: The following output is printed by your display() method:
# Title: The Alchemist
# Author: Paulo Coelho
# Price: 248

#=============================== Tutorial======================
#  https://www.geeksforgeeks.org/abstract-classes-in-python/
#  https://docs.python.org/3/library/abc.html
#  https://www.smartfile.com/blog/abstract-classes-in-python/
# In fact, Python on its own doesn't provide abstract classes. Yet, Python comes with a module which provides the infrastructure for 
# defining Abstract Base Classes (ABCs). This module is called - for obvious reasons - abc.


from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):      ##ABC can be replaced with metaclass=ABCMeta. ABCMetac is used for defining Abstract Base Classes(ABCs).  
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod           # A decorator indicating abstract methods
    def display(): pass

#Write MyBook class

class MyBook(Book):
    def __init__(self,title,author,price):
        super(MyBook).__init__()            ## You can use Book as a attribute here
        self.price = price

    def display(self):                     # need to put self other this there will be error 'display() takes 0 positional arguments but 1 was given'
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))           ## need to convert to string as it takes only string

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

























