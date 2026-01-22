#2. Write a lambda function which accepts one number and returns cube of that number.
Cube = lambda No : No ** 3

def main():
    Value = int(input("Enter Number: "))
    Ret = Cube(Value)
    print("Cube is: ",Ret)

if __name__ == "__main__":
    main()