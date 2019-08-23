# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


print('You have to enter the first two number as 0 and 1')
a = eval(input('Please enter how many fibonnaci numbers you wanna generate: '))
c = []


def fibonnaci():
    i = 2
    d = eval(input('Enter the first number. it need to be zero:'))
    c.append(d)
    e = eval(input('Enter the second number. It need to be one: '))
    c.append(e)
    print(c)
    for i in range(2,a):
        print(c[0])
        print(c[1])
        c[i] = c[i-1] + c[i-2]
        f = c[i]
        c.append(f)


fibonnaci()
print(c)









