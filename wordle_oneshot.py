secret_word = "python"

user_guess = input("What is your 6-letter guess? ").lower()

while len(user_guess) != 6:
    user_guess = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

wordle = ""

for i in range(len(secret_word)):
    if user_guess[i] == secret_word[i]:
        wordle += GREEN_BOX
    elif user_guess[i] in secret_word:
        wordle += YELLOW_BOX
    else:
        wordle+= WHITE_BOX
print(wordle)

if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")   