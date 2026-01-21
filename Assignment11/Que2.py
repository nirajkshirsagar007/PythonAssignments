# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountDigits(No):
    count = 0
    if(No == 0):
        return 1
    while No > 0:
        No = No // 10
        count = count + 1

    return count

def main():
    Value = int(input("Enter Number: "))
    Ret = CountDigits(Value)

    print("Count of Digits is: ",Ret)

if __name__ == "__main__" :
    main()
    
