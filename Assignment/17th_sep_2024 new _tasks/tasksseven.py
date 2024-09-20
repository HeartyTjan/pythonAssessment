total_scores = 0
score_count = 0
for count in range(1,11):
	scores = int(input("Enter Scores : "))
	
	if scores % 2 == 0 :
		total_scores += scores
		score_count += 1

average = total_scores / score_count 
print("Total sum of even scores is : ", total_scores)
print("Average of scores is : ", average);

