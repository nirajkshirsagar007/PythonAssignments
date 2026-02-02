# Q3) Display File Line by Line
#    Problem Statement:
#    Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
#    Input:
#    Demo.txt
#    Expected Output:
#    Display each line of Demo.txt one by one.

def DisplayLine(fName):
    
    try:
        with open(fName,"r") as fobj:
            for line in fobj:
                print(line)
               

    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    DisplayLine(FileName)

if __name__ == "__main__":
    main()