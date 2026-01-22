# 8. Write a lambda function which accepts two numbers and returns addition.

Addition = lambda No1, No2: No1 + No2 

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Ret = Addition(Value1,Value2)
    print("Addition is:",Ret)

if __name__ == "__main__":
    main()