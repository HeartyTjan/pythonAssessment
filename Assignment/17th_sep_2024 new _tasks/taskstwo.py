total_scores = 0
score_count = 0
for count in range(10):
	scores = int(input("Enter Scores : "))
	total_scores += scores
	score_count += 1

average = total_scores / score_count 

print("Average of scores is : ", average);