# Q1) Count Lines in a File
#    Problem Statement:
#    Write a program which accepts a file name from the user and counts how many lines are present in the file.
#    Input:
#    Demo.txt
#    Expected Output:
#    Total number of lines in Demo.txt.

def CountLines(fName):
    
    try:
        count = 0
        with open(fName,"r") as fobj:
            for line in fobj:
                count = count + 1
        print("Total no of lines are: ",count)
    
    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    CountLines(FileName)

if __name__ == "__main__":
    main()