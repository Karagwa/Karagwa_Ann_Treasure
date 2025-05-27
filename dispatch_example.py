from multipledispatch import dispatch
@dispatch(int, int, int)
def add(x, y, z):
    r = x + y + z
    print(f"Result of addition with three integers: {r}")
    
@dispatch(float, float)
def add(x, y):
    r = x + y
    print(f"Result of addition with two floats: {r}")

add(1, 2, 3)  # This will call the first function
add(1.5, 2.5)  # This will call the second function