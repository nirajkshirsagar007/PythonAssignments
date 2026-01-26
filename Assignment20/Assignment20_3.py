#3: Design a Python application that creates two threads named EvenList and OddList.
#   Both threads should accept a list of integers as input.
#   The EvenList thread should:
#        Extract all even elements from the list.
#       Calculate and display their sum.
#   The OddList thread should:
#       Extract all odd elements from the list.
#       Calculate and display their sum.
#   Threads should run concurrently.

import threading

lobj = threading.Lock()

def Display_Even_Sum(Data):
    Sum = 0
    with lobj:
        print("Even elements are: ")
        for i in Data:
                if i % 2 == 0:
                    print(i)
                    Sum = Sum + i

    print("Sum of Even numbers:",Sum)

def Display_Odd_Sum(Data):
    Sum = 0
    with lobj:
        print("Odd elements are: ")
        for i in Data:
                if i % 2 == 1:
                    print(i)
                    Sum = Sum + i

    print("Sum of Odd numbers:",Sum)

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]

    EvenList = threading.Thread(target=Display_Even_Sum,args=(Data,))
    OddList = threading.Thread(target=Display_Odd_Sum,args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("Exit from main")

if __name__ == "__main__":
    main()