#3: Design a Python application where multiple threads update a shared variable.
#   Use a Lock to avoid race conditions.
#   Each thread should increment the shared counter multiple times.
#   Display the final value of the counter after all threads complete execution.

import threading

counter = 0          
lock = threading.Lock()

def IncrementCounter():
    global counter
    for i in range(1000):       
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():
    t1 = threading.Thread(target=IncrementCounter, name="Thread-1")
    t2 = threading.Thread(target=IncrementCounter, name="Thread-2")
    t3 = threading.Thread(target=IncrementCounter, name="Thread-3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()

