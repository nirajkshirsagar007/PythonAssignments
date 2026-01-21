# 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 54321

def Numbers(No):
    for i in range( No,0 ,-1):
        print(i,end=" ")
        
def main():
    Value = int(input("Enter Number: "))

    Numbers(Value)

if __name__ == "__main__":
    main()