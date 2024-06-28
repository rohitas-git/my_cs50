# Classes are a way by which, in object-oriented programming, 
# we can create our own type of data and give them names.

# ... => simply means that we will later return to finish that portion of our code
# Notice by convention that Student is capitalized


class Student:
    # instance method
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    # a specific function by which you can print the attributes of an object if we wish
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"



def main():
    student = get_student()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()