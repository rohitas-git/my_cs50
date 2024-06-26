
def main():
    r = get_fuel_fraction()
    show_fuel(r)
    
    
def get_fuel_fraction():
    while True:
        x = get_int("Enter numerator: ")
        y = get_int("Enter denominator: ")
        if x is None or y is None:
            continue  # Re-prompt the user if x or y is None (invalid input)
        try:
            ratio = do_fuel_fraction(x, y)
            if ratio is not None:
                # print(f"Fuel fraction: {ratio}%")
                return ratio
        except ValueError:
            print("Numerator should not be greater than the denominator. Please try again.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please try again.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def do_fuel_fraction(x, y):
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if x > y:
        raise ValueError("Numerator should not be greater than the denominator.")
    return round(x * 100 / y)


def show_fuel(ratio):
    if ratio <=1:
        print('E')
    elif ratio >= 99:
        print('F')
    else:
        print(ratio)

main()