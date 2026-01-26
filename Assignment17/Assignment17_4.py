# 4. Write a program which accept one number form user and return addition of its factors.
#Input:12
#Output: 16  (1+2+3+4+6)

def SumFact(No1):
    Sum = 0
    for i in range(1,No1):
        if(No1 % i == 0):
            Sum = Sum + i

    return Sum


def main():
    Value1 = int(input("Enter Number: "))
    Ret = SumFact(Value1)
    print("Addition of Factors is: ",Ret)
    
if __name__ == "__main__":
    main()