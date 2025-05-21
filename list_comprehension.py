# List and dictionary comprehensions
# List comprehension

square =[x**2 for x in range(10)]
print(square)

# Dictionary comprehension
numbers=[1,2,3,4,5]
squared_dict = {x: x**2 for x in numbers}
print(squared_dict)

#List comprehension with condition
even_square = [x**2 for x in range(10) if x % 2 == 0]
print(even_square)

