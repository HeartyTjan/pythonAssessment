print("""
	 Calculate the Investment Return
		for 10,20,30 years

""")

principal = 1000
rate = 7/100
years = 10


for count in range(3):
	print("investment return for ", count * 10 + 10 , "years :", round(1000 * (1+ rate)**(count * 10 + 10),2))

	