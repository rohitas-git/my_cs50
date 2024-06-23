# a list is a list of multiple values and is ordered
# a dict associates a key with a value and is unordered

# list 
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]
mixBag = [1,"a", 2**10, "bcde", 3.0, True,]
print(mixBag)

# dict
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student, house in students.items():
    print(f"{student}: {house}")
print("--------------------------------------")

# data table: list of dicts
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")