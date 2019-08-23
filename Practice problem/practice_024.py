# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

## Text manipulation
# >>> prefix=' '*8
# >>> sep=' '*2
# >>> print("%sHello%sWorld." % (prefix, sep))
#     Hello  World.



a = eval(input("Enter the size of the board: "))

def tic_tac_toe():
    for i in range(a):
        j = '----'
        print(a*j)
        k = '|   '
        print((a+1)*k)
    print(a*j)
    

b = tic_tac_toe()
print(b)













