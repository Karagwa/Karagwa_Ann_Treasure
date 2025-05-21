#while can loop a set of statement as long as a condition is true

count=1
while count<=5:
    print(count)
    count+=1
    
#Break Statement
#break state ment is used to exit the loop prematurely, regardles of the loop's condition

#Exit a loop when x is 4
count=1
while count<=5:
    
    if count==4:
        break
    print(count)
    count+=1
    
#Continue Statement
#continue statement is used to skip the current iteration of a loop and continue with the next iteration
i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)
    
#Real World Example
#Example: Guessing Game
#Generate a random number between 1 and 10. Keep asking the user to guess the number until they get it right.    
import random
number_to_guess = random.randint(1, 10)
guess = 0

while guess != number_to_guess:
    guess= int(input("Guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print("Congratulations! You've guessed the number.")
    else:
        print("Try again!")