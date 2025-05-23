#python datatypes
# Inbuilt data types include string, list, tuple, set, dictionary, boolean, integer, float, complex
# User-defined data types include class, object, and function

z=30 #initializing a variable
print(z)
print(type(z)) #checking the type of the variable
print(isinstance(z, int)) #checking if the variable is an instance of a particular type

t= 2.5
print(t)
print(type(t))

#Strings
#Python is case sensitive
name="Livingston"
print(name)

name2="My name is Gloria"
print(name2)

name3="Afternoon Session"
print(name3)

name4="Arnold"
print(name4)

#comlex numbers
#complex_number= 5+7j
#2 is the real part and 3j is the imaginary part

r= 7+5j
print(r)
print(type(r))

y=6j
#remember there is a silent 0+6j

#Python list
#Store multiples items in a single variable

name = ["Stone", "Ronney", "Esther", "Boaz"]
print(name)

print(name[-1]) #prints the last item in the list

#List constructor
#List constructor is used to create a list from a tuple, set, or any other iterable
cars= list(("Toyota", "Nissan", "Honda", "Subaru"))
print(cars)

lisst5=[1, 2, 3, 4, 5]
print(lisst5)
lisst5.append(0) #adds 6 to the end of the list
print(lisst5)
print(type(lisst5))

array1= [1, 2, 3, 4, 5]
print(array1)
array1.append("Blue") # type: ignore #adds 6 to the end of the list
print(array1)

dict = {
    "name":"Stone",
    "age": 30,
    "Location":"Nairobi",
}

print(dict)