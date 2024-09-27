# Hoş geldiniz
# rastgele bir sayı belirle ve bunu yazdır
# 1 ile 100 arasında sayı girmelisiniz (yazı)
# zorluk seç easy - hard
# make a guess: (input)
# zor ise 5 kolay ise 10 hakkı var, her yanlış denemeye azalacak bu hak (attempts)
# sayıdan düşükse too low.
# sayıdan yüksekse too high
#https://patorjk.com/software/taag/#p=display&f=Tmplr&t=Cagri

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
random_number = random.choices(range(1, 100),k=1)
print(random_number[0])
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

def checker(user_guess,attempts):
    while attempts > 1:
        attempts -= 1
        if user_guess == random_number[0]:
            print("Congratulations!")
            break
        elif user_guess < random_number[0]:
            print("Too low")
        elif user_guess > random_number[0]:
            print("Too high")

        print("Guess again.")
        print(f"You have {attempts} attempts")
        user_guess = int(input("Make a guess: "))

    if attempts == 1:
        print("You lose! Please try again")
def guessing_game(attempts):
    user_guess = int(input("Make a guess: "))
    if choose_difficulty == "easy":
        attempts = 10
    elif choose_difficulty == "hard":
        attempts = 5

    checker(user_guess,attempts)


guessing_game(attempts)





