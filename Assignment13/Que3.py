# 3. Write a program which accepts one number and 
# checks whether it is perfect number or not.

def ChkPerfectNo(No):
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    if( Sum == No ):
        return True
    else:
        return False


def main():
    Value = int(input("Enter Number: "))
    Ret = ChkPerfectNo(Value)

    if (Ret == True):
        print("it is Perfect No.")
    else:
        print("It is not perfect no.")

if __name__ == "__main__":
    main()