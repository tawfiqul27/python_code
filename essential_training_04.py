# definition of function

# def main():
#     kitten('meaow', 'gree', 'purr')     # this is using arguments

#     # x = ('meaow','gree','purr')         # this using tuple
#     # kitten(*x)                          # you can define function with the tuple

# def kitten(*args):
#     if len(args):
#         for s in args:
#             print(s)
#     else:
#         print('Meeeeaow')

# if __name__ == '__main__':
#     main()
    
    
### this is the use of keyword arguments

# def main():
#     animal(Buffy='meaow', Zilla='gree', Angele='purr')
#     # x = dict(Buffy='meaow', Zilla='gree', Angele='purr')            # This is by defining a variable
#     # animal(**x)


# def animal(**kwargs):                                   # use two asterisk to pass dictionary value.
#     if len(kwargs):
#         for s in kwargs:
#             print('animal {} says {}'.format(s, kwargs[s]))
#     else:
#         print('Measwwwwww.')

# if __name__ == '__main__':
#     main()


##### Retruing the value

# def main():
#     x = kitten ()
#     print(type(x), x)

# def kitten():
#     print('Predator')
#     return(2323)

# if __name__ == '__main__':
#     main()
    

### A generator is a special class of function that serves as an iterator
# instead of returing a single value, the generator returens a stream of values
# learn more about genrator. Kichu bujhini

# def main():
#     for i in inclusive_range(25):
#         print(i, end=(' '))
#     print()


# def inclusive_range(*args):
#     numargs = len(args)
#     start = 0
#     step = 1

#     # initialize parameters
#     if numargs < 1:
#         raise TypeError(f'expected at least 1 argument, got {numargs}')
#     elif numargs == 1:
#         stop = args[0]
#     elif numargs ==2:
#         (start, stop) = args 
#     elif numargs == 3:
#         (start, stop, step) = args 
#     else:
#         raise TypeError(f'expected at most 3 arguments, got {numargs}')
        
#     # generator
#     i = start
#     while i <= stop:
#         yield i
#         i += step

# if __name__ == '__main__':
#     main()
    

### A decorator is a form of metaprogramming    

# def f1():
#     print('This is f1')

# f1()
# x = f1
# x()
# # ---------------
# def f1():       # f2 cannot be called outside of f1. f2 only exists inside the scope of f1.
#     def f2():   # so f1 can be said the wrapper of f2
#         print('This is f2')
#     return f2

# # x = f1()
# # x()

#--------------------

def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

@f1         # this is called decorator. which is same as f3=f1(f3)
def f3():
    print('This is f3')

f3 = f1(f3)
f3()

