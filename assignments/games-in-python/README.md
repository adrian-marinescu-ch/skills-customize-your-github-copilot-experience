# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python to practice string manipulation, control flow, and handling user input. By the end of this assignment, students will implement game logic, manage state, and provide clear user feedback.

## 📝 Tasks

### 🛠️ Build the Hangman game

#### Description
Implement a playable Hangman game using Python. Use the provided `starter-code.py` as a starting point or write your own implementation. The game should run in the terminal and allow a single player to guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list or the provided `data.csv` (one word per line).
- Display the current progress using underscores for unknown letters separated by spaces (for example: `_ a _ _ n`).
- Accept single-letter guesses (case-insensitive) and reveal matching letters in the progress display.
- Track and display letters already guessed and remaining incorrect attempts (e.g., "Incorrect guesses left: 6").
- Decrement the remaining attempts only for incorrect, non-repeated guesses; prevent repeated guesses from consuming attempts.
- End the game with a clear win message (showing the word) or a lose message with the correct word revealed.
- Organize code into functions (for example: `choose_word()`, `display_progress()`, `process_guess()`, `main()`), and keep `starter-code.py` style and comments where appropriate.

#### Example session
```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess! Progress: _ a _ _ _
Incorrect guesses left: 6
Guess a letter: z
Nope. Incorrect guesses left: 5
...
You win! The word was: 'apple'
```

Use the starter code in this folder (`starter-code.py`) to get started if you prefer a scaffolded approach.

