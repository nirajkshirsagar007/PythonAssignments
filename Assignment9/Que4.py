#4. Write a program which accepts one number and prints cube of that number.


def Cube(No):
        Ans = No * No * No
        return Ans
    
def main():
    Value = int(input("Enter number:"))
    
    Ret = Cube(Value)
    print("Cube of the number is: ",Ret)

if __name__ == "__main__":
    main()

    