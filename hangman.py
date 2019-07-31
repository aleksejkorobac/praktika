import random

words = open("wordlist.txt").read().splitlines()
theword = random.choice(words)
thewordlength = len(theword)
thewordhidden = "*" * thewordlength
thewordsplit = list(theword)
thewordhiddensplit = list(thewordhidden)

guessedword = False
tries = 6
triesleft = 6

print("")
print("Let's play a game of hangman. You have", tries,  "tries")

while guessedword == False:
    if triesleft == 0:
        print("--- You failed ---")
        print("--- The word is:", theword, "---")
        break

    print("The word is: ", ''.join(thewordhiddensplit))
    guess = input("Guess a letter: ")

    if (theword.find(guess)) == -1:
        triesleft = triesleft - 1
        if triesleft != 0:
            print("--- That ain't it chief. You have", triesleft, "tries left ---")
    else:
        for i in range (0,len(thewordsplit)):
            if thewordsplit[i] == guess:
                thewordhiddensplit[i] = guess
        if (''.join(thewordhiddensplit).find("*")) != -1:
            print("--- TRUE, you have", triesleft, "tries left ---")

    if (''.join(thewordhiddensplit).find("*")) == -1:
        print("")
        print("--- Congratulations you guessed the word! It was |", theword, "| ---")
        guessedword = True
        break
