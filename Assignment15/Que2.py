# 2. Write a lambda function using filter() which accepts a list of numbers
#  and returns a list of even numbers.

Even = lambda No : No % 2 == 0

def main():
    Data = [1,2,3,4,5,6,7,8,9]

    FData = list(filter(Even,Data))
    print("Even numbers are:",FData)


if __name__ == "__main__":
    main()