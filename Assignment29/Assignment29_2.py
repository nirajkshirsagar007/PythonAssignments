#Q2) Display File Contents
#    Problem Statement:
#    Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
#    Input:
#    Demo.txt
#    Expected Output:
#    Display contents of Demo.txt on console.
#

def Display(fName):

    try:
        fobj = open(fName,"r")
        
        Data = fobj.read()
        print("Data from the File is:")
        print(Data)
        fobj.close()
    except FileNotFoundError:
        print("File is not present.")


def main():
    FileName = input("Enter File name:")
    Display(FileName)

if __name__ == "__main__":
    main()
