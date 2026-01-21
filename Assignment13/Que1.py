# 1. write a program which accept length and width of the rectangle and print the area.

def Area(length,width):
    area = length*width
    print("Area of rectangle is : ",area)
        
def main():
    Value1 = int(input("Enter length: "))
    Value2 = int(input("Enter width: "))

    Area(Value1, Value2)

if __name__ == "__main__":
    main()