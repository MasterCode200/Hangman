import random
name = input("Hello, What is your name? ")
print("Best of Luck!" , name)
words = ["games","luck","exams","study","science","maths","netflix","instagram","food","goa","florida","coding","amazon","tesla","google","spotify","youtube","chocolate","pizza","coke","chips","dance","music","party"]
word = random.choice(words)

print("Guess the characters of the word!")
guesses = ''
turns = 12

while turns>0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1
    if failed ==0:
        print("You have won, Good Game, Congratulations!")
        print("The word is: ", word)
        break
    guess = input("guess a letter")
    guesses+=guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns,'more guesses')

        if turns==0:
            print("You lost, try ")




    
