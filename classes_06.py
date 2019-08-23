
# Workicng with classes

class myclass():
    def method1(self):          # object oriented terminology are called method
      print("myclass method1")

    def method2(self, someString): 
        print("myclass method2 " + someString )


class anotherclass(myclass):
    def method1(self):          # object oriented terminology are called method
      myclass.method1(self)
      print("aontherclass method1")

    def method2(self, someString): 
        print("anotherclass method2 ")


def main():
    c = myclass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherclass()
    c2.method1()
    c2.method2("This is a string")

if __name__ == '__main__':
    main()
    
    








