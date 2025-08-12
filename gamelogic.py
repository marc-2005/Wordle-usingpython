
import random
def pick_target(words):
    """Randomly pick a target word from the list of words."""
    return random.choice(words)
def feedback_for_guess(guess, target):
    feedback = [GRAY] * 5
    target_chars = list(target)
    guess_chars = list(guess)

    for i in range(5):
        if guess_chars[i] == target_chars[i]:
            feedback[i] = GREEN
            target_chars[i] = None
            guess_chars[i] = None

    # Second pass: yellows
    for i in range(5):
        if guess_chars[i] is None:
            continue
        if guess_chars[i] in target_chars:
            feedback[i] = YELLOW
            matched_index = target_chars.index(guess_chars[i])
            target_chars[matched_index] = None

    return ''.join(feedback)

