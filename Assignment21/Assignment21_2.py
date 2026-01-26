#2: Design a Python application that creates two threads.
#   Thread 1 should calculate and display the maximum element from an list.
#   Thread 2 should calculate and display the minimum element from the same list.
#   The list should be accepted from the user.

import threading

def FindMax(arr):
    print("Maximum element is:", max(arr))

def FindMin(arr):
    print("Minimum element is:", min(arr))

def main():
    Data = []

    Size = int(input("Enter number of elements: "))
    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    t1 = threading.Thread(target=FindMax, args=(Data,), name="MaxThread")
    t2 = threading.Thread(target=FindMin, args=(Data,), name="MinThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

