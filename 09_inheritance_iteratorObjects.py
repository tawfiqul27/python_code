# inheretance and iterator objects. I haved checked but need to work on it later


# class animal:
#     x = [1, 2, 3]                 # this list is actually a class variable but not an object variable
#     def __init__(self, type, name, sound):      # init is special method name. self indicates the object. type, name, and sound are the 
#         self._type = type           # these are object variable
#         self._name = name
#         self._sound = sound
    
#     def type(self, t = None):   
#         if t: self._type = t    
#         try: return self._type        ### this checks if the value is actually there or not. rather than return the value blindly.
#         except AttributeError: return None  # this exception tries to return a value. If that fails, it returns none instead


#     def name(self, q = None):
#         if q: self._name = q
#         return self._name
    
#     def sound(self, s = None):
#         if s: self.sound = s
#         return self._sound



###### Handling exceptions

import sys      # sys module has a lot of constant in it which provides a detail info about the error

def main():
    try:
        c = int('foo')
    except ValueError:
        print('I caught a ValueError')

    try:
        p = 5/0
    except ValueError:
        print('I caught a ValueError')
    except:       # exception can caught different types of error. like valueError and zerodivision error
        print(f'unknown error: {sys.exc_info()[1]}')

    try:
        l = 5/3
    except ZeroDivisionError:
        print('5 divided by 3 is not zero division error')
    except:
        print('Unknown error')
    else:
        print('good job!')
        print(l)
        


if __name__ == '__main__':
    main()
    

#### Reporting errors. This will caught error and report the error with the exact problem in the program
# def main():
#     try:
#         for i in inclusive_range(1,2,3,4):
#             print(i, end = ' ')
#         print()
#     excpt TypeError as e:
#         print(f'range error: {e}')

# if __name__ == '__main__':
#     main()







