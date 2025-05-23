import sys

print("Script starting...", flush=True)  # This will force immediate output

while True:
    try:
        print("About to ask for first number", flush=True)
        x = int(input("Enter a number: "))
        print("About to ask for second number", flush=True)
        y = int(input("Enter another number: "))
        if y == 0:
            print("You cannot divide by zero", flush=True)
            continue
        print("Let's divide the two numbers", flush=True)
        print(x / y, flush=True)
        break
    except ZeroDivisionError:
        print("You cannot divide by zero", flush=True)
    except ValueError:
        print("Please enter a valid number", flush=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", flush=True)
    finally:
        print("Let's do some division.", flush=True)

print("Script completed.", flush=True)

