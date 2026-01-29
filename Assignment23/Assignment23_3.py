# 3: Write a Python program to implement a class named Numbers with the following specifications:
#   
#   The class should contain one instance variable:
#       Value
#   Define a constructor (init) that accepts a number from the user and initializes Value.
#   Implement the following instance methods:
#       ChkPrime() returns True if the number is prime, otherwise returns False
#       ChkPerfect()returns True if the number is perfect, otherwise returns False
#       Factors()-displays all factors of the number
#       SumFactors() returns the sum of all factors
#       (You may use this method as a helper in ChkPerfect() if required)
#   Create multiple objects and call all methods.
#    
class Numbers:

    def __init__(self,No ):
        self.Value = No

    def ChkPrime(self):
        if (self.Value) <= 1: 
            return False
        for i in range(2, int(self.Value/2) +1):
            if(self.Value % i == 0):
                    return False
        else:
            return True       

    def Factors(self):
        print(f"Factors of {self.Value} are :")
        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                print(i,end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                sum = sum + i
        
        return sum

   
    def ChkPerfect(self):
        if(self.SumFactors == self.Value):
            return True
        else:
            return False

def main():
    obj1 = Numbers(6)
    obj2 = Numbers(11)

    print("Number: ",obj1.Value)
    print("Prime:",obj1.ChkPrime())
    print("Perfect:",obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors is: ",obj1.SumFactors())

    print("*"*30)

    print("Number: ",obj2.Value)
    print("Prime:",obj2.ChkPrime())
    print("Perfect:",obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors is: ",obj2.SumFactors())


if __name__ == "__main__":
    main()
