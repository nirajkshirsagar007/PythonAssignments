#2. Write a program which accept one number and display below pattern.
# Input:5
# Output: 
#       *   *   *   *   *    
#       *   *   *   *   *   
#       *   *   *   *   *   
#       *   *   *   *   *   
#       *   *   *   *   *   

def Display(No1):
    for i in range(No1):
        for j in range(No1):
            print("*",end="\t")
        print()

def main():
    Value1 = int(input("Enter Number: "))
    Display(Value1)
    
if __name__ == "__main__":
    main()