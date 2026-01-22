# 10. Write a lambda function which accepts three numbers and returns largest number.
Largest = lambda No1, No2: No1 if No1 > No2 else No2 

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Ret = Largest(Value1,Value2)
    print("Largest is:",Ret)

if __name__ == "__main__":
    main()