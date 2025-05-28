class Father:
    def skill(self):
        print("cooking, driving, and teaching")
        
class Mother:
    def skill(self):
        print("cooking, drawing, and teaching")
        
class Child(Mother, Father): # Inherits from both Mother and Father whereby Mother is the first in the method resolution order (MRO)
    pass

# Creating an object of the Child class
child = Child()
# Calling the inherited methods
child.skill()  # This will call the skill method from the Father class due to method resolution order (MRO)