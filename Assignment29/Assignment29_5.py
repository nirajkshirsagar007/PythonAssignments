# Q5) Frequency of a String in File
#    Problem Statement:
#    Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
#    Input:
#    Demo.txt Marvellous
#    Expected Output:
#    Count how many times "Marvellous" appears in Demo.txt.

def CountFrequency(fname, word):

    try:
        with open(fname, "r") as fobj:
            data = fobj.read()

            count = data.count(word)

            print("Frequency is:", count)

    except FileNotFoundError:
        print("File not found")


def main():
    filename = input("Enter file name: ")
    string = input("Enter string to search: ")

    CountFrequency(filename, string)


if __name__ == "__main__":
    main()
