# https://www.youtube.com/watch?v=MuFcvopLTD0
# 
# Task
# The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the 
# editor below. Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation
# for the divisorSum(n) method must return the sum of all divisors of n.

# Input Format: A single line containing an integer, n
# Constraints: 1<=n<=1000

# Output Format: You are not responsible for printing anything to stdout. The locked template code in the editor below will call 
# your code and print the necessary output.

# Sample Input
# 6

# Sample Output
# I implemented: AdvancedArithmetic
# 12

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        a = []
        for i in range(1,(n+1)):
            if n%i==0:
                a.append(i)
        # print(a)
        return sum(a)
        pass

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)  # This print the name of base class 
print(s)
