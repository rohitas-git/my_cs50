# Use of Tuple, List, Dictionary


# A tuple is a sequences of values
# Note: Unlike a list, a tuple can’t be modified

def main():
    student = get_student_dict()
    print(f"{student['name']} from {student['house']}")

def get_student_tuple():
    name = input("Name: ")
    house = input("House: ")
    return name, house # implicitly returns a tuple (name,house)

def get_student_list():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

def get_student_dict():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()