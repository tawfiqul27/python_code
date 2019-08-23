#!/usr/local/bin/pyhton3

# or 
#!/usr/bin/env pyhton3      # this is a common use to find pyhton interpreter. Is used mostly. This two commands works in linux or Macs. 


import platform    
# this will import module from a library.  
# the module may contain any combination of classes, functions or other pyhton objects

# version = platform.python_version()

# print('This is pyhton version is {}'.format(version)); print("Hello World")

def main():
    message()

def message():
    print('This is pyhton version is {}'.format(platform.python_version()))
    if True:    # if we put false then else will print
        print('Line number 1')
    else:
        print('Line number 2 or not true')


x = 42
print('Hello world at the age of {}'.format(x))

# another way of printing previous line in python3.6 is the use of f. f for format
print(f'Hello world at the age of {x}')


# the variables can be described as similar as C language. This is python 2
p = 31
print('Hello world at my age of %d ' %p)


# simple fibonacci series. The sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end= ' ', flush=True)  # flush=True will flush output buffer
    a, b = b, a + b


# simple for loop. For loop is more efficient than while loop

words = ['one', 'two', 'three', 'four']
for i in words:
    
    print(i)


# this program will check if this is a prime number

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 5
if isprime(n):
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')

# to get a list of prime numbers in a range
for n in range(100):
    if isprime(n):
        print(n, end='\n', flush=True)
    



#### Example of class. under class there could be functions or objects. Sometimes functions 
# are called methods, and variables inside a class is called properties


class Duck:
    sound = 'Quacccccck!'
    walking = 'Walk like a duck'
    def quack(self):    # self is not a keyword and it is used to be readable by everybody else
        print(self.sound)
    def walk(self):
        print(self.walking)

def dumpling():
    Amin = Duck()   # Amin is now an object of the class Duck
    Amin.quack()
    Amin.walk()

dumpling()


### Ternary conditional operator

hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

if __name__ == '__main__':
    main()
    




