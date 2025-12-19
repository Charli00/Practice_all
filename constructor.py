# create a class called student
# create a variable 
#  name and register number using constructor.

#  create a function called display which sholud display the name and register number of the student

class student:
    def __init__(self):
        self.name=""
        self.register=''
    def display(self):
        print("Name of the student : ",self.name)
        print("Register Number of the student : ",self.register)

jo=student()

jo.name="DJA"
jo.register=1231

jo.display()

