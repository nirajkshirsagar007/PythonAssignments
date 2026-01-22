# 3. Write a lambda function using filter() which accepts a list of numbers
#  and returns a list of odd numbers.

Odd = lambda No : No % 2 == 1

def main():
    Data = [1,2,3,4,5,6,7,8,9]

    FData = list(filter(Odd,Data))
    print("Odd numbers are:",FData)


if __name__ == "__main__":
    main()