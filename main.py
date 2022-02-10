import random

class WordLengthError(Exception):
	pass

class WordNotFoundError(Exception):
	pass

with open('words.txt') as f:
	WORDS = [word.strip() for word in f.readlines()]

secret = random.choice(WORDS).strip()
game_over = False
feedback = ""
lives = 6

while not game_over:
	boxes = ""
	print(f"You have {lives} guesses.\n")
	while True:
		guess = input("Guess a word: ").lower()
		try:
			if len(guess) != 5:
				raise WordLengthError
			elif guess not in WORDS:
				raise WordNotFoundError
		except WordLengthError:
			print("Guesses must be 5 letters long.\n")
		except WordNotFoundError:
			print("That guess isn't in our dictionary.\n")
		else:
			break

	for a, b in zip(secret, guess):
		# TODO: manage guesses with repeat letters
		if a == b:
			boxes += "🟩"
		elif b in secret:
			boxes += "🟨"
		else:
			boxes += "⬛"
	feedback += f"{guess.upper()} {boxes}\n"
	print(feedback)
	lives -= 1
	if guess == secret:
		game_over = True
		print("You win!")
	else:
		if lives == 0:
			game_over = True
			print(f"You lose - the word was {secret.upper()}")
			
