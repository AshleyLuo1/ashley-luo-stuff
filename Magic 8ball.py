#The random responses of the Magic 8ball will go into a list
#Import random will allow randomization of the strings in the answers list
import random
answers = ["It is certain.", "Yes.","Signs point to yes.",
           "Cannot predict now.", "Better not tell you now.", "Reply hazy, try again.",
           "Don't count on it.", "My reply is no.", "Very doubtful,"]

#Use a function to store the code for the Magic 8ball so it is easier to recall later in a loop
#Create a code that will ask user a question and spit out a random response from the list above
def question():
    question = input("What is your question for the Magic 8ball? ")
#Random.choice will randomize the responses in the answers list
    print(random.choice(answers))

#Use the while loop to continue asking user for questions until they respond with No
while True:
#Recall the function made earlier
    question()
    repeat = input("Do you have another question for the Magic 8ball? (Y/N) ")
    if repeat == "N" or repeat == "n":
        print("Thanks for playing!")
#Use the break to end the game when the user responds to the repeat question with no
        break