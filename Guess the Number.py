import random

print ("Welcome to the Guessing game!")
print ("Rules are as follows:")
print ("1. Guess a number between 0 and 100")
print ("2. You only get 3 tries")
print ("3. You get a hint each time you fail to guess the answer")
print ("Enjoy!")
print ("\n")

ch="Y"

while (ch!='N'):
    tries=3
    guess=int(input("Enter your number:"))
    number=random.randint(0,100)

    for i in range (0,3):

        if (guess==number):
            print ("YOU GUESSED IT RIGHT!")
            break

        elif (guess>number):
            print ("The guess is too high")
            print ("Try again")
            tries=tries-1

            if (tries == 0):
                break
            print ("You have",tries,"tries remaining")
            guess=int(input("Enter your number:"))
            
        elif (guess<number):

            print ("The guess is too low")
            print ("Try again")
            tries=tries-1

            if (tries == 0):
                break
            print ("You have",tries,"tries remaining")
            guess=int(input("Enter your number:"))

    if (tries==0):
        print ("Better luck next time")
        ch=input("Do you wish to try again? Y or N:\n")
        ch=ch.upper()