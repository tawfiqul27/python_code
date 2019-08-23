# Inheritance
# This allows you to establish a hierarchy for your classes. A class that inherits from some other class (referred to as a superclass) 
# is called a subclass. While a subclass inherits methods and behaviors from a superclass, it can also declare new fields and methods 
# (as well as override superclass methods).

# Subclass
# A subclass is defined with the extends keyword. For example, the syntax ClassB extends ClassA establishes ClassB as a subclass of 
# ClassA. Java only supports single inheritance, meaning a subclass cannot extend more than one superclass. Synonymous terms: derived 
# class, extended class, child class.

# Subclass Constructors
# Because a constructor initializes an instance of a class, they are never inherited; however, the subclass must call a superclass 
# constructor as it is an extension of a superclass object. This can be done in either of the two ways shown below. 

# Overriding Methods
# When overriding a method, it is best practice to precede the method with the @Override annotation. This signifies to both the reader
# and the compiler that this method is overriding an inherited method, and will also help you check your work by generating a compiler
# error if no such method exists in the superclass. Method overriding is demonstrated in the example below.

# Example
# Let's say a not-for-profit organization has an Employee class, and each instance of the Employee class contains the name and salary 
# for an employee. Then they decide that they need a similar-yet-different way to store information about volunteers, so they decide 
# to write a Volunteer class that inherits from Employee. This is beneficial because any fields and methods added to Employee will also
# be accessible to Volunteer. 

#=========================================================================================
# Problem:
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for 
# Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has parameters:
#     1. A string, firstName.
#     2. A string, lastName.
#     3. An integer, id.
#     4. An integer array (or vector) of test scores, scores.
# A char calculate() method that calculates a Student object's average and returns the grade character representative of their 
# calculated average:

# Grading Scale:
# Letter          Average(a)
#   O             90<=a<=100
#   E             80<=a<=90
#   A             70<=a<=80
#   P             55<=a<=55
#   D             40<=a<=55
#   T              a<40

# Input Format

# The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the 
# calculate method (which takes no arguments). You are not responsible for reading the following input from stdin:
# The first line contains firstName, lastName, and id, respectively. The second line contains the number of test scores. The third 
# line of space-separated integers describes scores.

# Constraints
# 1<=|firstName|,|lastName|<=10
# |id| = 7
# 0<=score,average<= 100

# Output Format
# This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() 
# method are properly implemented.

# Sample Input
# Heraldo Memelli 8135627
# 2
# 100 80

# Sample Output
# Name: Memelli, Heraldo
# ID: 8135627
# Grade: O

# Solution =======================================================================

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        # self.firstName = firstName
        # self.lastName = lastName
        # self.idNumber = idNumber
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a = sum(scores)/len(scores)     ## calculate the average of list of numbers
        if 90<=a<=100:
            grade = 'O'
            return grade
        elif 80<=a<=90:
            grade = 'E'
            return grade
        elif 70<=a<=80:
            grade='A'
            return grade
        elif 55<=a<=70:
            grade= 'P'
            return grade
        elif 40<=a<=55:
            grade = 'D'
            return grade
        elif a<40:
            grade = 'T'
            return grade
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())








