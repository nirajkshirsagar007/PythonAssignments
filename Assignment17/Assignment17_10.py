# 10. Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37

def SumDigits(No):

    temp = No
    Sum = 0
    while No != 0:
        temp = No % 10
        Sum = Sum + temp
        No = No//10
    
    return Sum

def main():
    
    Value = int(input("Enter Number: "))
    Ret = SumDigits(Value)

    print("Sum of Digits of the Number: ",Ret)


if __name__ == "__main__":
    main()