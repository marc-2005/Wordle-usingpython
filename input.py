# Geting a valid gues
def get_guess(valid_words):
    """Prompt the player for a guess and validate it."""
    while True:
        guess = input('Enter your guess (5 letters): ').strip().lower()

        if len(guess) != 5:
            print('Please enter a 5-letter word.')
            continue
        if not guess.isalpha():
            print('Please use only alphabetic characters.')
            continue
        if guess not in valid_words:
            print('This word is not in the list')
            continue

        return guess

