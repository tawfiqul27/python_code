# Example of sets

# def main():
#     a = set("I want to go to itly but will not stay")
#     # a = { 2, 5, 113, 7, 9 }     this is also a list. list is a collection of un-sorted data item 
#     b = set("I'm sorry that I couldn't make it happen")
#     print_set(a)
#     #print_set(b)
#     print(sorted(b))
#     print(a -b )
#     print(a | b)

# def print_set(o):
#     print('{', end=' ')
#     for x in o: 
#         print(x, end = ' ')
#     print('}')

# if __name__ == '__main__':
#     main()
    


##### List comprehensive is a list created based on another list or another list

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = [ x for x in seq if x % 3 != 0 ] 
    seq4 = [ (x, x**2) for x in seq]
    from math import pi
    seq5 = [round(pi,i) for i in seq]
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
def print_list(o):
    for i in o:
        print(i, end=' ')

if __name__ == '__main__':
    main()
    

###### Mixed structure. I didn't check. Need to check later



