#4: Design a Python application that creates two threads.
#   Thread 1 should compute the sum of elements from a list.
#   Thread 2 should compute the product of elements from the same list.
#   Return the results to the main thread and display them.

import threading

def CalculateSum(Data, Result, lock):
    temp = 0
    for i in Data:
        temp = temp + i

    with lock:
        Result["sum"] = temp

def CalculateProduct(Data, Result, lock):
    temp = 1
    for i in Data:
        temp = temp * i

    with lock:
        Result["product"] = temp

def main():
    Data = []

    Size = int(input("Enter number of elements: "))
    print("Enter elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = {}          
    lock = threading.Lock()

    t1 = threading.Thread(target=CalculateSum,args=(Data, Result, lock),name="SumThread")

    t2 = threading.Thread(target=CalculateProduct,args=(Data, Result, lock),name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", Result["sum"])
    print("Product of elements:", Result["product"])
    print("Exit from main")

if __name__ == "__main__":
    main()


