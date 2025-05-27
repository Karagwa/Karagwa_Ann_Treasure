#Abtraction
#A class that contains one or more abstract methods.


from abc import ABC, abstractmethod #Abraction

# Starting a car engine and bike

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass #This method has no implementation in the abstract class
    
    
# Child class implementing the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

# Derived class implementing the abstract method
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")
        
# Notes :
# We cannot create an instance of the abstract class Vehicle directly.
# We can only create instances of the derived classes Car and Bike.

car1 = Car()
car1.start_engine()  # Output: Car engine started.