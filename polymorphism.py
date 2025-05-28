#polymorphism

#Polymorphism is the ability to present the same interface for different data types.

class Bird:
    def fly(self):
        print("Bird is flying")
        
class Eagle(Bird):
    def fly(self):
        print("Eagle is soaring high in the sky")
        
class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flapping its wings quickly")
bird= Bird()

def fly_bird(bird: Bird):
    bird.fly()
            
eagle1= Eagle()
sparrow1 = Sparrow()

# DEmonstrating polymorphism
fly_bird(eagle1)  # Output: Eagle is soaring high in the sky        
fly_bird(sparrow1)  # Output: Sparrow is flapping its wings quickly

                