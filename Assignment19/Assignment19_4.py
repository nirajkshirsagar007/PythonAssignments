# 4. Write a program which contains filter(), map() and reduce() in it. 
#    Python application which contains one list of numbers. 
#    List contains the numbers which are accepted from user. 
#    Filter should filter out all such numbers which are even. 
#    Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

def ChkEven(No):
    return No % 2 == 0

def CalculateSquare(No):
    return No**2

def Addition(A,B):
    return A + B

def main():
    Data = []

    Size = int(input("Enter No of Elements: "))
    print("Enter Elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkEven,Data))
    print("List After Filter is:",FData )

    MData = list(map(CalculateSquare,FData))
    print("List After map: ",MData)

    RData = reduce(Addition,MData)
    print("Output of reduce is: ",RData)


   
if __name__ == "__main__":
    main()