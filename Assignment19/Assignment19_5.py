# 5. Write a program which contains filter(), map() and reduce() in it. 
#    Python application which contains one list of numbers. 
#    List contains the numbers which are accepted from user. 
#    Filter should filter out all prime numbers. Map function will multiply each number by 2. 
#    Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# 
# Input List t = [2, 70, 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    if(No<=1):
        return False

    for i in range(2,No):
        if(No % i == 0):
            return False
    
    else:
        return True


def Multiply(No):
    return No*2

def Maximum(A,B):
    return A if A > B else B
 
def main():
    Data = []

    Size = int(input("Enter No of Elements: "))
    print("Enter Elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime,Data))
    print("List After Filter is:",FData )

    MData = list(map(Multiply,FData))
    print("List After map: ",MData)

    RData = reduce(Maximum,MData)
    print("Output of reduce is: ",RData)


   
if __name__ == "__main__":
    main()