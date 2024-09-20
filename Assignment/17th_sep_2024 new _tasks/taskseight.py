total_scores = 0
score_count = 0

while True :
	scores = int(input("Enter Scores : "))
	
	if scores > 0 and scores < 100 :
		total_scores += scores
		score_count += 1
		
	if score_count == 10 :
		break


print("Total sum of even scores is : ", total_scores)


