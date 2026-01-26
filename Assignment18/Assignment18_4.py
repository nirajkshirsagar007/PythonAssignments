# 4. Write a program which accept N numbers from user and store it into List. 
#    Accept one another number from user and return frequency of that number from List.
# Input: Number of elements: 11
# Input Elements:13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5
# Output: 3

def CountElement(Arr,No):
    Count = 0

    for i in range(len(Arr)):
        if Arr[i] == No:
            Count = Count + 1
        
    return Count

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
    
    Value2 = int(input("Enter Element to search: "))
    
    Ret = CountElement(Data,Value2)
    print("Count of element is : ",Ret)

if __name__=="__main__":
    main()

    