import random
tries = 10
random_number = random.randint(0,100)
previous_guesses = []
play = True
while play:
    while tries>0:
        print("Tries left: ",tries)
        user_guess = int(input("Your guess: "))
        if user_guess == random_number:
            print("Congratulations! You guessed the number",random_number,"correctly with",tries,"tries left")
            play = False
            break
        if user_guess in previous_guesses:
            print("You already tried this number before")
        elif user_guess > 100 or user_guess < 0:
            print("The number can't be less than 0 or more than 100")
        elif user_guess>random_number:
            tries-=1
            print("The number is smaller than your guess")
        elif user_guess<random_number:
            tries-=1
            print("The number is bigger than your guess")
    if play:
        play_again_choice = input("You finished all your attempts\n Play again?\n Y) yes\n N) no\n")
        if play_again_choice.upper() == "Y":
            tries=10
        else:
            play=False