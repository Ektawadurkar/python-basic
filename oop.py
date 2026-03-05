class Student:
    
    # constructor
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # method to display student info
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# creating objects
s1 = Student("Rahul", 20, 85)
s2 = Student("Vikrant", 19, 90)

# calling method
s1.display()
print("------")
s2.display()
