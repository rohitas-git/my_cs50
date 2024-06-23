
def main():
    get_number()
    iterateList()
    
    for _ in range(3):
        print("meow")
    students = ["Hermoine", "Harry", "Ron"]
    for student in students:
        print(student)
    for i in range(len(students)):
        print(i + 1, students[i])
    
    
# using loops as a way of validating the input of the user.
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def iterateList():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in myList:
        print(number, end = " ")
        
        
main()