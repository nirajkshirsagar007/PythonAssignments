# Q4) Copy File Contents into Another File
# Problem Statement:
#    Write a program which accepts two file names from the user.
#    First file is an existing file
#    Second file is a new file
#    Copy all contents from the first file into the second file.
# Input:
#    ABC.txt Demo.txt
# Expected Output:
#   Contents of ABC.txt copied into Demo.txt.

def DisplayLine(fName1, fName2):
    
    try:
        with open(fName1,"r") as fobj1 ,open(fName2,"w") as fobj2 :
            Contents = fobj1.read()

            fobj2.write(Contents)

        print(f"Contents are copied from {fName1} into {fName2} successfully.")

    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName1 = input("Enter existing File name:")
    FileName2 = input("Enter new File name:")

    DisplayLine(FileName1, FileName2)

if __name__ == "__main__":
    main()