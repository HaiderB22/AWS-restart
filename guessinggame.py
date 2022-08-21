import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isguessright = False

while isguessright  != True: 
    guess = input("guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. That is correcr! you win!".format(guess))
        isguessright = True
    else:
        print("you guessed {}. Sorry your wrong dumb dumb".format(guess))
        
        
