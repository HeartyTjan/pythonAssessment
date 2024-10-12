text = "123abcd568efg672bagdj15g3h4v5h"

size = len(text)
modified_text = ""
for count in range(size):

	letter = text[count]
	#print(letter)
	
	if not letter.isdigit():
 
		modified_text += letter
		

print(modified_text)


