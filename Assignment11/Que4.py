# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321
def ReverseNumber(No):
    Rev = 0
    
    while No > 0:
        reminder = No % 10
        Rev = Rev * 10 + reminder
        No = No // 10

    return Rev

def main():
    Value = int(input("Enter Number: "))
    Ret = ReverseNumber(Value)

    print("Reversed Number is: ",Ret)

if __name__ == "__main__" :
    main()
    
