# 1. Write a program which accept N numbers from user and store it into List. 
#    Return addition of all elements from that List.
# Input: Number of elements: 6
# Input Elements: 13 5 45 7 4 56
# Output: 130 

def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of elemens:  ")
    Size = int(input())

    Data = list()

    print("Enter the Elements: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    Ret = Summation(Data)
    print("Summation is : ",Ret)

if __name__=="__main__":
    main()

    