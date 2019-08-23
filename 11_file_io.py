# file I/O 
#########################################
#########################################
# Open file

# def main():
#     f = open('lines.txt')       # open('lines.txt','r') r will open the file in read mode, w for write, a for append mode, r+ for read and write mode 
#     # r+b for binary mode, r+t for text mode
#     for line in f:
#         print(line.rstrip())

# if __name__ == '__main__':
#     main()
    
    
###############################################
###############################################
# Working with Text files 

def main():
    infile = open('/home/islamam/Desktop/python_scripts/Essential_training_LinkedIN/lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)  # outfile.writelines(line)  does the same thing as this
        print('.', end=' ')
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()
    














