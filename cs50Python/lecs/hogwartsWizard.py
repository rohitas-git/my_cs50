
# both Student and Professor inherit the characteristics of Wizard. 
# Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard 
# as the line super().__init__(name) runs the init method of Wizard.

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

# It just so happens that exceptions come in a heirarchy, 
# where there are children, parent, and grandparent classes. These are illustrated below:

# BaseException
#  +-- KeyboardInterrupt
#  +-- Exception
#       +-- ArithmeticError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- KeyError
#       +-- NameError
#       +-- SyntaxError
#       |    +-- IndentationError
#       +-- ValueError
#  ...