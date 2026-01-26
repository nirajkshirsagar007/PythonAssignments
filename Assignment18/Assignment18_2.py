# 2. Write a program which accept N numbers from user and store it into List. 
#   Return Maximum number from that List.
# Input: Number of elements: 7
# Input Elements: 13 5 45 7 4 56 34
# Output: 56

def Maximum(Arr):
    Max = Arr[0]

    for i in range(len(Arr)):
        if Arr[i] > Max:
            Max = Arr[i]
        
    return Max

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
    
    Ret = Maximum(Data)
    print("Maximum is : ",Ret)

if __name__=="__main__":
    main()

    