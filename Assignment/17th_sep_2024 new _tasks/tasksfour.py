total_scores = 0
score_count = 0
for count in range(1,11):
	scores = int(input("Enter Scores : "))
	
	if count % 2 == 0 :
		total_scores += scores

print("Total sum of scores is : ", total_scores)





