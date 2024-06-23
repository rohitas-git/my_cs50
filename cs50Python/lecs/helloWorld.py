# single line comment
"""
multi-
line comment
"""

def main():
    helloName()
    helloFullName()
    

def helloName(name = "World"):
    print(f"Hello, {name}") 
    
def helloFullName():
    name = input("What's your name? ").strip().title()
    first, last = name.split(" ")
    print(f"Hello, {name}", end= "??? \n") 
    print("Name:", first, last, sep=" > ") 
    
main()