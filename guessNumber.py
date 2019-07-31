import random
min = 1
max = 5

while True:
    print("")
    print("Wanna play a game? yes/no")
    yesno = input()
    if yesno == "no":
        break
    if yesno == "yes":
        random_number = random.randint(min, max)
        print("")
        print("Guess the randomly generated number from",min, "to", max)
        while True:
            guess = (input())
            try:
                val = int(guess)
                if val < min or val > max:
                    print("Please enter a number from ", min, "to ", max)
                    continue
                else:
                    break
            except ValueError:
                print("---------- Please enter an integer ----------")
                continue
    else:
        print("")
        print("---------- yes or no answers only plz ----------")
        continue

    if val == random_number:
        print ("Congratulations you guessed correctly!")
    if val < random_number:
            print("--- Big oof, you guessed too low and didn't get it ---")
            print("--- The number was:" ,random_number, "---")
    if val > random_number:
            print("--- Yikes you guessed too high and didn't get it ---")
            print("--- The number was:" ,random_number, "---")
