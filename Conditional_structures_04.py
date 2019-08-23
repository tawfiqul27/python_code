# working with conditional statements

def main():
    x, y =10, 100
    p, q= 100, 100


    # conditional flow uses if, elif, else
    if (x<y):
        st = "x is less than y"
    
    print(st)

    if (p<q):
        less= "p is less than q"
    elif (p==q):
        less= "p is equal to q"
        
    else:
        less= "p is greater than q"

    print(less)


    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x<y) else "x is greater than or the same as y"
    print(st)

if __name__ == '__main__':
    main()
    






