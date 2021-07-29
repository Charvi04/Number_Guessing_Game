# This is a number guessing game in which you need to guess a number between 1 and 9. Lets see if you can the number in 5 moves.

import random

# Creating the variables here
player_name = input("Hello, What is your name ? ")
number_of_guesses = 5
number = random.randint(1, 9)

# Showing the greeting and question to the user
print('Hello '+player_name+", I am guessing a number between 1 to 9, can you guess the number :-")

# Checking if the answer written by the user is correct or not and telling it to the user
while number_of_guesses != 0:
    guess = int(input())
    number_of_guesses -= 1
    if guess < number:
        print("You number is too low but you could still try for some time")
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print('Well Done, YOU WON !!')
        break