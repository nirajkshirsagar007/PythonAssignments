#4: Design a Python application that creates three threads named Small, Capital, and Digits.
#   All threads should accept a string as input.
#   The Small thread should count and display the number of lowercase characters.
#   The Capital thread should count and display the number of uppercase characters.
#   The Digits thread should count and display the number of numeric digits.
#   Each thread must also display:
#       Thread ID
#       Thread Name

import threading

lobj = threading.Lock()

def CountSmall(Data):
    count = 0
    with lobj:
        for ch in Data:
            if ch.islower():
                count = count+1
        
        print("----Small Thread----")
        print("Thread id:",threading.get_ident())
        print("Thread Name:",threading.current_thread().name)
        print("Lowercase Count :", count)
        

def CountCapitl(Data):
    count = 0
    with lobj:
        for ch in Data:
            if ch.isupper():
                count = count+1

        print("----Capital Thread----")
        print("Thread id:",threading.get_ident())
        print("Thread Name:",threading.current_thread().name)
        print("Uppercase Count :", count)

def CountDigits(Data):
    count = 0
    with lobj:
        for ch in Data:
            if ch.isdigit():
                count = count+1

        print("----Digits Thread----")
        print("Thread id:",threading.get_ident())
        print("Thread Name:",threading.current_thread().name)
        print("Digit Count :", count)

def main():
    String = input("Enter String: ")

    Small = threading.Thread(target=CountSmall,args=(String,),name="Small")
    Capital = threading.Thread(target=CountCapitl,args=(String,),name="Capital")
    Digits = threading.Thread(target=CountDigits,args=(String,),name="Digits")
 
    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main")

if __name__ == "__main__":
    main()