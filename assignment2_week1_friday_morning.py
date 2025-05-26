

while True:
    try:
        
        x = int(input("Enter a number: "))
        
        y = int(input("Enter another number: "))
        if y == 0:
            print("You cannot divide by zero")
            continue
        print("Let's divide the two numbers")
        print(x / y)
        break
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Let's do some division.")



