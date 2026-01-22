# 4. Write a lambda function which accepts two numbers and returns Minimum number.

Maximum = lambda No1,No2 :No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))
    Ret = Maximum(Value1, Value2)
    print("Minimum is: ",Ret)

if __name__ == "__main__":
    main()