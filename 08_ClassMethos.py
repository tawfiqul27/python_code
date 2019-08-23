## Class methods and object data
### A function that is associated with a class is called method. this provides 
## the interface to the class and its object

class animal:
    x = [1, 2, 3]                 # this list is actually a class variable but not an object variable
    def __init__(self, type, name, sound):      # init is special method name. self indicates the object. type, name, and sound are the 
        self._type = type           # these are object variable
        self._name = name
        self._sound = sound
    
    def type(self, t = None):    # these are called accessors or getters
        if t: self._type = t    # object variable self._type is called private variable which is defined with self method followed with underscore. 
        return self._type        ### contd' Private variable should not be set or retrived outside of the setter getter.
        
    def name(self, q = None):
        if q: self._name = q
        return self._name
    
    def sound(self, s = None):
        if s: self.sound = s
        return self._sound


    def __str__(self):          # str is another special method like init
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = animal('kitten', 'fluffy', 'rwar')
    a1 = animal('duck', 'donald', 'quack')
    print(a0)
    print(a1)
    print(animal('velociraptor', 'veronica', 'hello'))
    
    print(a0.x)
    a1.x[0] = 9
    print(a1.x)


if __name__ == '__main__':
    main()











