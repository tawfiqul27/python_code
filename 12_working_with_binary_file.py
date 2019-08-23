
#### This will use an image and cpoy it ot another image. Image is a binary file


def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin_copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end=' ')
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()
    











