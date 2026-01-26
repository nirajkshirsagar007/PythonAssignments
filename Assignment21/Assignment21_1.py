#1: Design a Python application that creates two threads named Prime and NonPrime.
#    Both threads should accept a list of integers.
#    The Prime thread should display all prime numbers from the list.
#    The NonPrime thread should display all non-prime numbers from the list.

import threading

lobj = threading.Lock()

def IsPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def DisplayPrime(Data):
    with lobj:
        print("---- Prime Thread ----")
        print("Thread ID:", threading.get_ident())
        print("Thread Name:", threading.current_thread().name)
        for no in Data:
            if IsPrime(no):
                print(no, end=" ")
        print("\n")

def DisplayNonPrime(Data):
    with lobj:      
        print("---- NonPrime Thread ----")
        print("Thread ID:", threading.get_ident())
        print("Thread Name:", threading.current_thread().name)
        for no in Data:
            if not IsPrime(no):
                print(no, end=" ")
        print("\n")

def main():
    Data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    Prime = threading.Thread(target=DisplayPrime, args=(Data,), name="Prime")
    NonPrime = threading.Thread(target=DisplayNonPrime, args=(Data,), name="NonPrime")

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
