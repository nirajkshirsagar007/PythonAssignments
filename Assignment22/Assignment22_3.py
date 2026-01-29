#3: Write a Python program to implement a class named Arithmetic with the following characteristics:
#   The class should contain two instance variables: Valuel and Value2.
#   Define a constructor (init) that initializes all instance variables to 0.
#   Implement the following instance methods:
#       Accept() accepts values for Valuel and Value2 from the user.
#       Addition() - returns the addition of Valuel and Value2.
#       Subtraction() returns the subtraction of Valuel and Value2.
#       Multiplication() - returns the multiplication of Valuel and Value2.
#       Division() - returns the division of Valuel and Value2 (handle division by zero properly).
#   Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:

    def __init__(self):
        self.Valuel = 0
        self.Value2 = 0

    def Accept(self):
        self.Valuel = int(input("Enter First No:"))
        self.Value2 = int(input("Enter Second No:"))

    def Addition(self):
        return self.Valuel + self.Value2

    def Substraction(self):
        return self.Valuel - self.Value2    
    
    def Multiplication(self):
        return self.Valuel * self.Value2

    def Division(self):
        if(self.Value2 == 0):
            print("Can't divide by zero")
            return
        else:
            return self.Valuel / self.Value2

def main():
    obj1 = Arithmetic()
    
    obj1.Accept()
    print("Addition is:",obj1.Addition())
    print("Substraction is: ",obj1.Substraction())
    print("Multiplication is: ",obj1.Multiplication())
    print("Division is: ",obj1.Division())

    print("-"*30)

    obj2 = Arithmetic()

    obj2.Accept()
    print("Addition is:",obj2.Addition())
    print("Substraction is: ",obj2.Substraction())
    print("Multiplication is: ",obj2.Multiplication())
    print("Division is: ",obj2.Division())

if __name__ == "__main__":
    main()
