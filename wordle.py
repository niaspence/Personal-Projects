
secret_word = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"



turns = 0
 

while turns <= 6:
    wordle = ""
    turns += 1
    print("=== Turn", turns, "/6 ===")
    guess = input("Enter your 5-letter guess: ").lower()
    if len(guess) != 5:
        guess = input("That wasn't 5 chars! Try again: ").lower()

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            wordle += GREEN_BOX
        elif guess[i] in secret_word:
            wordle += YELLOW_BOX
        else:
            wordle+= WHITE_BOX
    if guess == secret_word:
        print("You won in", turns, "/ 6 turns!")
        print(wordle)
        break

    print(wordle)

if turns == 7:
    print("X/6 - Sorry, try again tomorrow!")