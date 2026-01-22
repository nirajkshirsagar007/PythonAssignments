# 5. Write a lambda function which accepts one number and 
# returns True if number is even otherwise False.

ChkEven = lambda No1: True if No1 % 2 == 0 else False

def main():
    Value = int(input("Enter Number: "))

    Ret = ChkEven(Value)
    print("is Even:",Ret)

if __name__ == "__main__":
    main()