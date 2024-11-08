'''
zero_array = [[0]*5]*4

zeros = 0

for row in zero_array:

	for column in row:

		print(column, end= " ")

	print()	

for index in range(len(zero_array)):

	for count in range(len(zero_array[0])):

		print(zero_array[index][count],end = " ")

	print()


zeros = [[0]*4 for i in range(5)]

for row in zeros:
	
	for item in row:
		
		print(item, end = " ")

	print()

zeros = [0]

zeros *= 5

lst_zeros = []
for _ in range(4):
	lst_zeros.append(zeros)


for row in lst_zeros:
	
	for item in row:
		
		print(item, end = " ")

	print()
'''
while True:

	try:
	
		row = int(input("Enter row : "))

		column = int(input("Enter column : "))
		
		if row < 0 or column < 0:

			print("Please input a reasonable value")
		else:

			lst_multiple = [[0]*column for _ in range(row)]

			for row in range(len(lst_multiple)):

				for column in range(len(lst_multiple[row])):

					lst_multiple[row][column] += (row*column) 

			for row in lst_multiple:
	
				for item in row:
				
					print(f"{item:6}",end = " ")

				print()
		
			break
	except:	
		print("Invalid input")






























