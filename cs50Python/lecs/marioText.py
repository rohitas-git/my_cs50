def main():
    print_square(3)
    pyramid(3)


def print_square(size):
    for _ in range(size):
        print_row(size)
        

def pyramid(n):
    for i in range(n):
        print("#" *(i+1))


def print_row(width):
    print("#" * width)


if __name__ == "__main__":
    main()