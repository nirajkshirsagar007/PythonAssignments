# Q4) Compare Two Files (Command Line)
#   Problem Statement:
#   Write a program which accepts two file names through command line arguments and compares the contents of both files.
#   If both files contain the same contents, display Success
#   Otherwise display Failure
# Input (Command Line): Demo.txt Hello.txt
# Expected Output: Success OR Failure

import sys

def Compare(fname1,fname2):

    try:
        with open(fname1,"r") as f1,open(fname2,"r") as f2:
            Data1 = f1.read()
            Data2 = f2.read()
            if (Data1 == Data2):
                print("Success")
            else:
                print("Failure")     
            
    except FileNotFoundError:
            print("File Not Found")


def main():
    if(len(sys.argv)!=3):
        print("Invalid Number of Arguments")
        print("python programFile_name <File1> <File2>")
        return

    Compare(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()
