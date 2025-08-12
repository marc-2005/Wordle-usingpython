## Project Overview
This project is a Python-based implementation of the popular **Wordle** game.  
The player has **6 attempts** to guess a randomly selected 5-letter word from a dataset.  
After each guess, the program provides feedback using colored markers:

- 🟩  – Correct letter in the correct position.
- 🟨  – Correct letter but in the wrong position.
- ⬛ – Letter is not in the target word.

The game ensures:
- All guesses are valid words from the dataset.
- Progress is displayed after each attempt.
- The game ends when the correct word is guessed or attempts are exhausted.

---

## 📂 Folder Structure
there are 5 folders 
- words.txt : this is the dictionary for the game
- main.py : This is the interface of the game 
- input.py :this is responsible for handling inputs 
- gamelogic.py : this is the core of the game and handles the logical flow of the game 
- wordlist.py : this handls reading the words from the file 


# 🔍 Logical Structure of the Code

### **1. Data Loading**
- **File:** `main.py` → `load_words()`
- Loads all valid 5-letter words from the `words` file.
- If `words` file does not exist, it creates one with default words.

### **2. Target Word Selection**
- **File:** `main.py` → `pick_target()`
- Randomly selects a word from the loaded list.

### **3. User Input Validation**
- **File:** `main.py` → `get_guess()`
- Prompts the user to enter a guess.
- Validates:
  - Guess is exactly 5 letters.
  - Guess contains only alphabetic characters.
  - Guess exists in the dataset.

### **4. Feedback Generation**
- **File:** `main.py` → `feedback_for_guess()`
- Compares guessed word with target word.
- Assigns color markers based on:
  - Correct letter & position (🟩)
  - Correct letter but wrong position (🟨)
  - Letter not present (⬛)

### **5. Game Loop**
- **File:** `main.py` → `main()`
- Runs up to 6 attempts.
- Stores and displays history of guesses.
- Ends game when:
  - Player guesses correctly.
  - All attempts are used.
