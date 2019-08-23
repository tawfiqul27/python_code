# Using standard modules

import datetime
import sys      # sys is a module
import os       # this will print OS related 
import random

def main():
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day)

    v = sys.version_info            # version_info is an element inside the class of an module
    p = sys.platform                # this will print the name of the platform
    q = os.name
    r = os.getenv('PATH')           # this will print path
    w = os.getcwd()
    x = os.urandom(25).hex()
    y = random.randint(10, 1099)
    z = list(range(25))


    print('Python version {}.{}.{}'.format(*v))
    print(p)
    print(q)
    print(r)
    print(w)
    print(x)
    print(y)
    print(z)
    random.shuffle(z)
    print(z)


if __name__ == '__main__':
    main()
    

### I have escaped 'creating module' tutorials














