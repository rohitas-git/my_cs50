# Possible bugs: 
# syntax error
# runtime error
# logic error

def main():
    pyramid(3)


def pyramid(n):
    for i in range(n):
        print("#" *(i+1))
                
# clicking a breakpoin at main and then stepping into it during debug run
if __name__ == "__main__":
    main()