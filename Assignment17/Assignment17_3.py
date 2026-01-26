# 3. Write a program which accept one number from user and return its factorial.
# Input:5
# Output: 120 

def Factorial(No1):
    Fact = 1
    for i in range(1,No1+1):
        Fact = Fact * i
    return Fact

def main():
    Value1 = int(input("Enter Number: "))
    Ret = Factorial(Value1)
    print("Factorial of number is: ",Ret)
    
if __name__ == "__main__":
    main()