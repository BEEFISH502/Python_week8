
#9) Guessing Game (While Loop)
def guessing_game():
    secret = 7
    attempts = 0
    while True:
        guess = int(input('Guess the number: '))
        attempts += 1
        if guess == secret:
            print(f'Correct! Guesses: {attempts}')
            break
        else:
            print(f'Nope, try again.')
guessing_game()