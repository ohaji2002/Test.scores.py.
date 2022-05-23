def main():
	#State variables: Track number of guesses, set the correct answer, and declare the user input variable guess
	correct_answer = 8
	guess = -1
	num_attempts = 0
	#Loop until the user guesses correctly
	while guess != correct_answer:
		#Get the input from the user and convert it to an integer
		guess = int(input("Guess the number between 1 and 20: "))
		num_attempts += 1
		#Give hint to the user OR if they got it right display the number of attempts
		if guess > correct_answer:
			print("Your guess was too high!")
		elif guess < correct_answer:
			print("Your guess was too low!")
		else:
			print("Correct! It took you", num_attempts, "tries")

main()
