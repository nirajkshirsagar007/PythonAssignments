# 2: Write a Python program to implement a class named BankAccount with the following requirements:
#    The class should contain two instance variables:
#       Name (Account holder name)
#       Amount (Account balance)
#    The class should contain one class variable:
#       ROI (Rate of Interest), initialized to 10.5
#    Define a constructor _ init) that accepts Name and initial Amount.
#    Implement the following instance methods:
#       Display()- displays account holder name and current balance
#       Deposit() accepts an amount from the user and adds it to balance
#       Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
#       CalculateInterest() calculates and returns interest using formula:
#       Interest =  (Amount * ROI) / 100
#   Create multiple objects and demonstrate all methods.
#    
class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount
        
    def Display(self):
        print(f"Account holder name: {self.Name}")
        print(f" Current balance: {self.Amount}.")

    def Deposit(self,amount):
        if amount > 0:
            self.Amount += amount
            print(f"Deposited {amount}.New balance:{self.Amount}")
        else:
            print("Deposite amount must be positive.")

    def Withdraw(self,amount):
        if(amount>0 and amount <=self.Amount):
            self.Amount -= amount
            print(f"Withdrew {amount}. New Balance: {self.Amount}")
        elif amount > self.Amount:
            print("Insufficient Funds.")
        else:
            print("Withdrawl amount must be positive.")
        

    def CalculateInterest(self):
        interest =  (self.Amount * self.ROI) / 100
        return interest

def main():
    account1 = BankAccount("Niraj",1000)
    account2 = BankAccount("Suraj",500)

    print("------Account 1 details------")
    account1.Display()
    account1.Deposit(200)
    account1.Withdraw(50)
    interest1 = account1.CalculateInterest()
    print(f"Calculated interest: {interest1}")
    account1.Withdraw(2000)

    print("------Account 2 details------")
    account2.Display()
    account2.Deposit(100)
    account2.Withdraw(50)
    interest2 = account2.CalculateInterest()
    print(f"Calculated interest: {interest2}")


if __name__ == "__main__":
    main()
