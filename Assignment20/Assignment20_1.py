#1: Design a Python application that creates two separate threads named Even and Odd.
# - The Even thread should display the first 10 even numbers.
# - The Odd thread should display the first 10 odd numbers.
# - Both threads should execute independently using the threading module.
# - Ensure proper thread creation and execution.
import threading

lobj = threading.Lock()

def Display_Even():
    for i in range(10):
        with lobj:
            print(f"Even:{2*i}")

def Display_Odd():
    for i in range(10):
        with lobj:
            print(f"Odd:{2*i+1}")

def main():
    Even_thread = threading.Thread(target=Display_Even)
    Odd_thread = threading.Thread(target=Display_Odd)

    Even_thread.start()
    Odd_thread.start()

    Even_thread.join()
    Odd_thread.join()


if __name__ == "__main__":
    main()