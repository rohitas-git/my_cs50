
def sq(x):
    return x*x

def isEven(x):
    return x % 2 == 0

def processInputs(x=0, y=0):
    if x == 0 or y == 0:
        x = float(input("x: "))
        y = float(input("y: "))
    z = round(x+y)
    print(f"Sum: {z}")
    z = x/y
    print(f"Division: {z:.2f}")

def main():
    print(2/3)
    print(3//2)
    print(3*2)
    print(3+2)
    print(3-5)
    print( round(22/7.0, 3) )
    print(sq(5))
    print(isEven(5))
    processInputs(2, 3)


if __name__ == "__main__":
    main()
