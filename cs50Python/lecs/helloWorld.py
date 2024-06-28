# single line comment
"""
multi-
line comment
"""

def main():
    print(helloName("David"))
    # helloFullName()
    

def helloName(name = "world"):
    return f"hello, {name}" 
    
def helloFullName():
    name = input("What's your name? ").strip().title()
    first, last = name.split(" ")
    # print(f"Hello, {name}", end= "??? \n") 
    # print("Name:", first, last, sep=" > ") 
    
if __name__ == "__main__":
    main()
    