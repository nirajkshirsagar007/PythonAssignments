# 3. Write a program which accept N numbers from user and store it into List. 
#   Return Minimum number from that List.
# Input: Number of elements: 4
# Input Elements: 13 5 45 7 
# Output: 5

def Minimum(Arr):
    Min = Arr[0]

    for i in range(len(Arr)):
        if Arr[i] < Min:
            Min = Arr[i]
        
    return Min

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
    
    Ret = Minimum(Data)
    print("Minimum is : ",Ret)

if __name__=="__main__":
    main()

    