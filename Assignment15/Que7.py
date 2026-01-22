#7. Write a lambda function using filter() which accepts a list of strings 
# and returns a list of strings having length greater than 5.

StrList = lambda x: len(x) > 5

def main():
    Data = ['Apple','Banana','Grapes','Cherry','Guava']

    RData = list(filter(StrList,Data))
    print("list of strings having length greater than 5:",RData)


if __name__ == "__main__":
    main()