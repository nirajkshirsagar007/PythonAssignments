# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input: 11
# Output: Positive Number
# Input: -8
# Output: Negative Number
# Input: 0
# Output: Zero

def Display(No):
    if(No > 0):
        print("Positive Number.")
    elif(No<0):
        print("Negative Number")
    else:
        print("Zero")

        
def main():
    Value = int(input("Enter Number: "))

    Display(Value)

if __name__ == "__main__":
    main()

