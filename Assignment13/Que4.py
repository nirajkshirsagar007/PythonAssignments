# 4. Write a program which accepts one number and prints binary equivalent.

def DisplayBinary(No):
    if(No == 0):
        return "0"
    else:
        temp = No
        Binary = ""
        while temp > 0:
            Reminder = temp % 2
            Binary = str(Reminder) + Binary
            temp = temp // 2

    return Binary

def main():
    Value = int(input("Enter Number: "))
    Ret = DisplayBinary(Value)
    print("binary equivalent of number is:",Ret)

if __name__ == "__main__":
    main()