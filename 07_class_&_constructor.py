###  Creating a class

# class Duck:
#     sound = 'Quack quack'       # these are data in the form of variable
#     movement = 'walks like a duck'

#     def quack(self):            # method in the form of function. The parameter of the method is self which is not a keyword 
#         print(self.sound)       # you can use any other word other than self
    
#     def move(self):
#         print(self.movement)

# def main():
#     donald = Duck()     # here donald is the object
#     donald.quack()
#     donald.move()
#     # print(donald.sound)    this will print the same thing of donald.quack()
    

# if __name__ == '__main__':
#     main()
    

### Constructing an object
class animal:
    def __init__(self, type, name, sound):      # init is special method name. self indicates the object. type, name, and sound are the 
        self._type = type           # these are object variable
        self._name = name
        self._sound = sound
    
    def type(self):         # these are called accessors or getters
        return self._type
    
    def name(self):
        return self._name
    
    def sound(self):
        return self._sound


def print_animal(o):
    # if not isinstance(o,animal):
    #     raise TypeError('print_animal(): requires an animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = animal('kitten', 'fluffy', 'rwar')
    a1 = animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(animal('velociraptor', 'veronica', 'hello'))
    
if __name__ == '__main__':
    main()
        
















