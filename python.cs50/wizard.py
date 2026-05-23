# Inheritance in oop
class Wizard:
    def __init__(self, name): 
        if not name:
            raise ValueError("Missing name")
        self.name = name 


# Creating sub classes

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) # Connect the super class to the sub-classes
        self.house = house



class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # connet the super class to the sub-classes
        self.subject = subject

    
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")