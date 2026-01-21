# 2. Write a program which accepts radius of circle and prints area of circle.

def Area(r):
    pi = 3.14159
    area = pi * r * r 
    print("Area of Circle is : ",area)
        
def main():
    Radius = int(input("Enter Radius: "))

    Area(Radius)

if __name__ == "__main__":
    main()