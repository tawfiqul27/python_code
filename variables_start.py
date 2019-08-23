# example file for variables

# declae a variables and initialize it

f=0
print(f)

# re-declare the variable works
f="abc"
print(f)

# ERROR: variable of different types cannot be combined 

print ("this is a string " + str(123))

# Global vs. local variables in functions

g=3

def someFunction():
    global g                # if you make the variable g global then g=3 won't take effect and everywhere the value of g will be def
    g="def"
    print(g)

someFunction()
print(g)

del g                 # the will delete the definition of f that was previously defined 
print(g)              # this will through an NameError: name 'g' is not defined  


