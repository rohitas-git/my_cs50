def main():
    x = int(input("x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")
    
    name = input("What's your name? ").strip().title()
    match name:
        case "Harry" | "Ron" | "Hermione":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
        

# python expression: return True if x % 2 == 0 else False
def is_even(x):
    return x % 2 == 0



main()