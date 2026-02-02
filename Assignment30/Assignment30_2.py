# Q2) Count Words in a File
#    Problem Statement:
#    Write a program which accepts a file name from the user and counts the total number of words in that file.
#    Input:
#    Demo.txt
#    Expected Output:
#    Total number of words in Demo.txt.

def CountWords(fName):
    
    try:
        count = 0
        with open(fName,"r") as fobj:
            for line in fobj:
                words = line.split()
                count = count + len(words)
            
            print(f"Total number of words in {fName} is: ",count)

    except FileNotFoundError:
        print("File Not Found")


def main():
    FileName = input("Enter File name:")
    CountWords(FileName)

if __name__ == "__main__":
    main()