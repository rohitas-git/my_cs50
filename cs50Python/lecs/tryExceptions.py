def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
    x = gentle_get_int()
    print(f"x is {x}")


# Python way: using try & except
def get_int(prompt):    
    while True:
        try:
            return int(input(prompt))
        except:
            print('Input should be integer')    


def gentle_get_int():
    while True:
        try:
            return int(input("Enter integer: "))
        except:
            pass 
    

# not so python: check with if
def get_int_2():
    while True:
        x = input("Enter integer: ")
        if x.isnumeric():
            return int(x)
        continue
        

main()