# Q5) Search a Word in File
#    Problem Statement:
#    Write a program which accepts a file name and a word from the user and checks whether that word is present in
#    the file or not.
#    Input:
#    Demo.txt Marvellous
#    Expected Output:
#    Display whether the word Marvellous is found in Demo.txt or not.

def DisplayLine(fName1, word):
    
    try:
        with open(fName1,"r") as fobj1:
            Contents = fobj1.read()

            if word in Contents:
                print("Word is found in File")
            else:
                print("Word is not present.")
           
    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName1 = input("Enter File name:")
    FileName2 = input("Enter Word to search in file:")

    DisplayLine(FileName1, FileName2)

if __name__ == "__main__":
    main()