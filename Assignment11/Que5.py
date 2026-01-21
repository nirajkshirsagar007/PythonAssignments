# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def ChkPalindrome(No):
    Temp = No
    Rev = 0
    
    while No > 0:
        reminder = No % 10
        Rev = Rev * 10 + reminder
        No = No // 10

    if Rev == Temp:
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number: "))
    Ret = ChkPalindrome(Value)

    if(Ret == True):
        print("Number is palindrome")
    else:
        print("Number is Not a palindrome")
        

if __name__ == "__main__" :
    main()
    
