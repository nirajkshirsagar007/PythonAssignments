#5: Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# 
# Ensure that:
#   Thread2 starts execution only after Thread1 has completed.
#   Use appropriate thread synchronizatio

import threading

lobj = threading.Lock()

def Display():
    with lobj:
        for i in range(1,51):
            print(i)

def DisplayRev():
    with lobj:
        print("Display in Reverse Order:")
        for i in range(50,0,-1):
            print(i)

def main():

    Thread1 = threading.Thread(target=Display,name="Thread1")
    Thread2 = threading.Thread(target=DisplayRev,name="Thread2")
 
    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()