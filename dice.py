min = 1
max = 6

import random

print("You rolled" ,random.randint(min, max))

while 1:

    roll_again = "no"
    print("Ayy wanna roll again? yes/no")
    roll_again = input()
    if roll_again == "yes":
        print("You rolled" ,random.randint(min, max))
    else:
        break
