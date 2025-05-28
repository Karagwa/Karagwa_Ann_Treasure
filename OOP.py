#inheritance

#superclass / base class /parent class
class Animal:  #blueprint for creating objects
    def speak(self):
        print("Animal make sound")
        
#subclass / derived class / child class
class Cat(Animal):  #inherits from Animal
    def sound(self):
        print("Cat makes sound meow")
        
#creating an object of the Cat class
cat = Cat()

#calling the inherited method
cat.speak()  

#call the child class method
cat.sound()  