# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4
# Output: 16
# Input: 6
# Output: 36

#def PowerOf(No):
#    Power = No**2

#   return Power

PowerOf = lambda No : No**2

def main():

    Value = int(input("Enter Number: "))

    Ret = PowerOf(Value)

    print("Power of two is: ",Ret)

if __name__ == "__main__":
    main()