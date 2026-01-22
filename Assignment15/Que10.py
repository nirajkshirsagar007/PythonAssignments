# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.


CountEven = lambda x: x % 2 == 0

def main():
    Data = [1,2,3,4,5,6]

    RData = len(list(filter(CountEven,Data)))
    print("CountEven is:",RData)


if __name__ == "__main__":
    main()