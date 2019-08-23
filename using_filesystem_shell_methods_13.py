# Working with filesystem shell methods
#


import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("/home/islamam/Desktop/python_scripts/textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("/home/islamam/Desktop/python_scripts/textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy over the permission, modification times, and other info
        shutil.copy(src, dst)       # this will copy the file
        shutil.copystat(src, dst)   # this will copy modification time and other metadata associated with the file
        
        # rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        # new put things into a zip archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)        

        # more fine-grained control over ZIP file. This will write to the zip file
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")



if __name__ == '__main__':
    main()
    


















