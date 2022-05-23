def main():
	print("Welcome! Please enter your test scores below (enter 999 to exit)")
	#Variables for tracking entered scores, number of scores, total accumulated score, and the average of the scores
	in_score = 0
	num_scores = 0
	total_score = 0
	avg_score = 0
	#Loop until the user enters 999 to quit
	while in_score != 999:
		#Get user's input score and also convert it to an integer
		in_score = int(input())
		#Verify the score before adding, otherwise display error if invalid
		if in_score >= 0 and in_score <= 100:
			total_score += in_score
			num_scores += 1
		elif in_score != 999:
			print("Invalid score entered: ", in_score)


	#Verify at least 1 score was entered (handle division by 0) and then calculate the average
	if num_scores > 0:
		avg_score = total_score / num_scores
		#Round average to two decimal places
		avg_score = round(avg_score, 2)

	#Display results to the user
	print("The total score was:", total_score)
	print("The average of the scores was:", avg_score)

main()