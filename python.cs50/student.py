""" name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}") 
"""

"""
def main():
    name = get_name
    house = get_house
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")



def get_house():
    return input("House: ")


if __name__ == "__main__":
    main() 
"""
#Another approach
'''
def main():
    name, house = get_student()
    print(f"{name} from house {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house #this is a tuple. 

if __name__ == "__main__":
    main()
'''

# Another Approach (An improvement to the former)

# def main():
#     student = get_student() # Changing the variable into a single variable called student.
#     print(f"{student[0]} from house {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # Adding a bracket to make it a readable tuple.

# if __name__ == "__main__":
#     main()

# You can override a tuple using a list to change items 
# def main():
#     student = get_student() # Changing the variable into a single variable called student.
#     print(f"{student[0]} from house {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house] # A list 

# if __name__ == "__main__":
#     main()



# # Another Approach using a Dictionary
# def main():
#     student = get_student() 
#     print(f"{student['name']} from house {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student 

# if __name__ == "__main__":
#     main()

# Another Approach using a Dictionary
def main():
    student = get_student() 
#   Showcasing the mutability of dictionary
    if student["name"] == "Ejiro":
        student["house"] = "Sunday"
    print(f"{student['name']} from house {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()