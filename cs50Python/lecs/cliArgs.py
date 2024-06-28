
# sys is a module that allows us to take arguments at the command line.

from sys import argv
from sys import exit

def main():
    # hello_1()
    # hello_2()
    hello_3()


def hello_1():
    try:
        name = argv[1]
    except IndexError:
        print("Usage: [NAME]")
    else:
        print("hello, my name is", name)
    

def hello_2():
    if len(argv) < 2:
        exit("Too few arguments")
    elif len(argv) > 2:
        exit("Too many arguments")
    print("hello, my name is", argv[1])
    
    
def hello_3():
    if len(argv) < 2:
        exit("Too few arguments")
    for arg in argv[1:-1]:
        print("hello, my name is", arg)
    
    
    
    
main()

