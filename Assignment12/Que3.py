# 3. Write a program which accepts two numbers and prints 
#    addition, subtraction, multiplication and division.

def Calculation(No1,No2):
    def Addition():
        Ans = No1 + No2
        print("Addition is : ",Ans)
    
    def Subtraction():
        Ans = No1 - No2
        print("Substraction is : ",Ans)

    def Multiplication():
        Ans = No1 * No2
        print("Multiplication is : ",Ans)
    def Division():
        if(No2 == 0):
            print("Division by zero is not possible.")
            return
        
        else:
            Ans = No1 / No2
            print("Division is : ",Ans)
    
    Addition()
    Subtraction()
    Multiplication()
    Division()

def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter second Number: "))
    
    Calculation(Value1,Value2)

if __name__ == "__main__":
    main()