# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6
def SumDigits(No):
    Sum = 0
    
    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter Number: "))
    Ret = SumDigits(Value)

    print("Sum of Digits is: ",Ret)

if __name__ == "__main__" :
    main()
    
