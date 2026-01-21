# 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 12345

def Numbers(No):
    for i in range(1, No + 1):
        print(i,end=" ")
        
def main():
    Value = int(input("Enter Number: "))

    Numbers(Value)

if __name__ == "__main__":
    main()