# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number

def ChkPrime(No):
    if(No > 1):
        for i in range(2,(No//2)+1):
            if(No % i == 0):
                return False
            else:
                return True
    else:
        return False
    
def main():
    Value = int(input("Enter Number: "))
    Ret = ChkPrime(Value)
    if(Ret == True):
        print(f"{Value} is Prime number.")
    else:
        print(f"{Value} is Not Prime number.")
    
if __name__ == "__main__":
    main()