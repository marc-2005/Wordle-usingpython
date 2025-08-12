import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WORDS_FILE = os.path.join(BASE_DIR, 'data', 'words.txt')

def load_words(filename=WORDS_FILE):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"'{filename}' not found. Creating a new one with sample words...")
        # Create file with some default words if no one exitexist ( I made it bec the file downloaded from internet could not be opened so I created the fil and added all wordds )
        default_words = [
            "apple", "berry", "charm", "delta", "eagle",
            "fancy", "giant", "happy", "joker", "lemon"
        ]
        with open(filename, 'w', encoding='utf-8') as f:
            for word in default_words:
                f.write(word + "\n")
        lines = default_words

    words = [w for w in lines if len(w) == 5 and w.isalpha()]


    return words
