def main():
    guess(x=10)

def guess(x):
    import random
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


if __name__ == "__main__":
    main()