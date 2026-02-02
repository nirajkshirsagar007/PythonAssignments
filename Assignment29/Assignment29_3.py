# Q3) Copy File Contents into a New File (Command Line)
#   Problem Statement:
#   Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
#   Input (Command Line):
#   ABC.txt
#   Expected Output:
#   Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys

def CopyFile(src):

    try:
        with open(src,"r") as fsrc,open("Demo.txt","w") as fDest:
            Data = fsrc.read()
            fDest.write(Data)
            print("Data Coppied Successfully.")

    except FileNotFoundError:
            print("File Not Found")


def main():
    if(len(sys.argv)!=2):
        print("Invalid Number of Arguments")
        print("Please specify name of the Directory")
        return

    fileName = sys.argv[1]
    CopyFile(fileName)
    
if __name__ == "__main__":
    main()
