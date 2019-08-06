import random
save_file = open("passwords.txt", "w+")

def check_integer(integer): #Checks if the input is an integer
    while True:
        try:
            int(integer)
            break
        except ValueError:
            integer = input("--- Please enter a number: ")
            continue
    return integer

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
characters = '!@#$%^&*'
Continue = True

while Continue == True:
    print("Password Generator 1.0")
    print("======================")
    while True:

        ans = input("Do you want to generate random passwords? yes/no: ")
        if ans.lower() == "yes":
            password_count = check_integer(input("How many passwords would you like to generate? "))
            password_length =  check_integer(input("How long do you want your passwords to be? "))
            password_list = []
            for j in range(int(password_count)):
                newpass = random.choice(letters).upper() + random.choice(characters)
                for i in range(int(password_length)-2):
                    newpass += random.choice(random.choice(letters) + random.choice(numbers) + random.choice(characters) + random.choice(letters).upper())
                password_list.append(newpass)

            Continue = False
            break

        elif ans.lower() == "no":
            Continue = False
            break

        else:
            print("Please answer with yes or no")
            continue

print("")
print("----- Here are your passwords -----")
i =0

for password in password_list:
    i+=1
    print("[",i,"]", password)

Continue = True
while Continue == True:
    print("")
    save_prompt = input("Do you want to save these passwords? yes/no ")
    if save_prompt.lower() == "yes":
        save_prompt_count = input("Which passwords would you like to save? ex '1,2,5' or 'all' ")
        try:
            if save_prompt_count.lower() == "all":
                for password in password_list:
                    save_file.write(password)
                    save_file.write("\n")
                print("--- Passwords saved! ---")
                break
            else:
                save_prompt_count_list = (save_prompt_count.split(","))
                for i in save_prompt_count_list:
                    save_file.write(password_list[int(i)-1])
                    save_file.write("\n")
                print("--- Passwords saved! ---")
                break
        except IndexError:
            print("Please select a password")
            continue
    elif save_prompt.lower() == "no":
        break

    else:
        print("Please answer with 'yes' or 'no'")
        continue
