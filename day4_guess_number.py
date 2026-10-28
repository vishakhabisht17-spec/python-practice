import random

def guess_number_game():
    print("🎯 Guess The Number (1-100)")
    secret = random.randint(1, 100)
    attempts = 0

    while attempts < 7:
        try:
            guess = int(input(f"Attempt {attempts+1}/7: "))
        except ValueError:
            print("Enter valid number!\n")
            continue
        
        attempts += 1
        if guess == secret:
            print(f"🎉 Correct in {attempts} tries!")
            break
        elif guess < secret:
            print("Too Low!\n")
        else:
            print("Too High!\n")
    else:
        print(f"Game Over! Number was {secret}")

guess_number_game()
