# 6. Write a lambda function which accepts one number and 
# returns True if number is odd otherwise False.

ChkOdd = lambda No1: True if No1 % 2 == 1 else False

def main():
    Value = int(input("Enter Number: "))

    Ret = ChkOdd(Value)
    print("is Odd:",Ret)

if __name__ == "__main__":
    main()