#2: Design a Python application that creates two threads named EvenFactor and OddFactor.
#   Both threads should accept one integer number as a parameter.
#   
# The EvenFactor thread should:
#       Identify all even factors of the given number.
#       Calculate and display the sum of even factors.
#   The OddFactor thread should: 
#       Identify all odd factors of the given number.
#       Calculate and display the sum of odd factors.
#   After both threads complete execution, the main thread should display the message:
#       "Exit from main"

import threading

lobj = threading.Lock()

def Display_Even_fact(No):
    Sum = 0
    for i in range(1,No+1):
        with lobj:
            if No % i == 0:
                if i % 2 == 0:
                    Sum = Sum + i

    print("Sum of Even Factor:",Sum)

def Display_Odd_fact(No):
    Sum = 0
    for i in range(1,No+1):
        with lobj:
            if No % i == 0:
                if i % 2 == 1:
                    Sum = Sum + i

    print("Sum of Odd Factor:",Sum)

def main():
    No1 = 20

    EvenFactor = threading.Thread(target=Display_Even_fact,args=(No1,))
    OddFactor = threading.Thread(target=Display_Odd_fact,args=(No1,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()