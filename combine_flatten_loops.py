def guessing_game():
    while True: 
        print("guess")
        guess = input()

        if guess == '42':
            print('correct guess')
            return False
        else:
            print(f'No, {guess} is not correct, try again\n')

guessing_game()
