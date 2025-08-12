def main():
    words = load_words()
    target = pick_target(words)
    max_attempts = 6
    history = []

    print('WORDLE GAME!')
    print(f'You have {max_attempts} attempts to guess a 5-letter word.')
    print("All guesses must be a valid word and in the 'words' file.")


    for attempt in range(1, max_attempts + 1):
        print(f'\nAttempt {attempt} of {max_attempts}')
        guess = get_guess(words)
        fb = feedback_for_guess(guess, target)
        history.append((guess, fb))

        print('\nYour progress:')
        for g, f in history:
            print(f + '  ' + g.upper())

        if guess == target:
            print(f"\nYou guessed the word in {attempt} attempt(s)")
            break
    else:
        print(f"\nOut of attempts. The word was: {target.upper()}")


if __name__ == '__main__':
    main()
appl