class Student:

    def __init__(self, name, age, marks):
        # instance variables
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# creating objects
s1 = Student("Diya", 19, 90)
s2 = Student("Siya", 20, 85)

s1.display()
s2.display()
