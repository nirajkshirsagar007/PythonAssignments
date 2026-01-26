# 9. Write a program which accept number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

def CountDigits(No):

    temp = No
    count = 0
    while temp != 0:
        count = count + 1
        temp = temp//10
    
    return count

def main():
    
    Value = int(input("Enter Number: "))
    Ret = CountDigits(Value)

    print("Count of Digits of the Number: ",Ret)


if __name__ == "__main__":
    main()