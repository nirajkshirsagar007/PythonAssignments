# 1. Write a lambda function using map() which accepts a list of numbers 
# and returns a list of squares of each number.

Square = lambda No : No**2

def main():
    Data = [1,2,3,4,5,6,7,8,9]

    MData = list(map(Square,Data))
    print("Square of numbers are:",MData)


if __name__ == "__main__":
    main()