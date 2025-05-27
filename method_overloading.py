# method overloading we have two or methods with same names but different parameters
# unlike java, python does not support method overloading
def add(a, b): # type: ignore
    r= a + b
    print(f"Result of addition: {r}")
    
    

    
    
    
# This will not work as expected because the second definition of add will override the first one
add(1, 2)  # This will raise an error because the first add is overridden
#add(1, 2, 3)  # This will work as expected
# This is because python considers the last defined function with the same name as the one to be used.
# To achieve similar functionality, you can use default parameters or variable-length arguments.

#Solution using default parameters
def add(a, b, c=0):
    r = a + b + c
    print(f"Result of addition: {r}")
    
add(1, 2)  # This will work and print 3
add(1, 2, 3)  # This will work and print 6

#pip refers to preferred installer program, it is a package manager for python
# it allows you to install and manage python packages

