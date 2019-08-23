# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

num = []

def max_num(n):
    for i in range(n):
        d = eval(input())
        num.append(d)
        print(num)
        if i >= 2:
            if num[i] > num[i-1] and num[i] > num[i-2]:
                print('The largest number is {}'.format(num[i]))
            elif num[i-1] > num[i-2] and num[i-1] > num[i]:
                print('The largest number is {}'.format(num[i-1]))
            else:
                print('The largest number is {}'.format(num[i-2]))
            break
        else:
            continue
    return num 


e = max_num(3)
print(e)









