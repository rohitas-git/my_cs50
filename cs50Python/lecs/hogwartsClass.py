# Classes are a way by which, in object-oriented programming, 
# we can create our own type of data and give them names.

# ... => simply means that we will later return to finish that portion of our code
# Notice by convention that Student is capitalized

# Properties can be utilized to harden our code. 
# In Python, we define properties using function “decorators”, which begin with @

# With house as a property, we gain the ability to 
# define how some attribute of our class, _house, should be set and retrieved.

# house is a property of our class, with functions via which a user attempts to set our class attribute. 
# _house is that class attribute itself. 
# Note: _house should only be set through the house setter.

# No hard constraints in Python 
# (nothing stopping from circumventing all of these properties, setters, getters)
# No notion of visibility, private or public in Python

# It's just on honor system for python (with honor follow the conventions)
# - If an instance variable starts with _, please don't touch it lest you want to break things
# - __varName => please really don't touch it

# int, str, float are classes
# same for list, tuple, dict

# instance methods: methods associated with obj of a class
# class methods: methods associated with class itself
# static method: 

class Student:
    # instance method
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # __str__ meant for user display
    # __repr__ meant for dev display
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name
    
    # Getter for house
    @property  # defines house as a property of our class.
    def house(self):
        return self._house
    
    # class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in self.houses:
            raise ValueError("Invalid house")
        self._house = house



def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()