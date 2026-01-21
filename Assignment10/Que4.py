# 4. Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10
def Even(No):
    
    for i in range(2,No+1,2):    
        print(i,end=" ")

def main():
    Value = int(input("Enter Number : "))

    Even(Value)
    

if __name__ == "__main__":
    main()