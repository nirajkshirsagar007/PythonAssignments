#Q1) Check File Exists in Current Directory
#   Problem Statement:
#   Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
#   Input:
#   Demo.txt
#   Expected Output:
#   Display whether Demo.txt exists or not.

import os

def ChkFile(fName):

    if os.path.exists(fName):
        print("File is Present")
    else:
        print("File is Not Present")

def main():
    FileName = input("Enter File name:")
    ChkFile(FileName)

if __name__ == "__main__":
    main()
