print("""
	
	Filling Status in USA
       =======================

	0 --> Single filers
	1 --> Married filling jointly
	2 --> Married filling separately
	3 --> Head of household
""")

option = int(input("Enter preferred option : "))



balance = 0
first_tax = 0	

match option :

	case 0 : 
		 amount = float(input("Enter income amount: "))

		 if amount < 0:

		 	print("Enter valid amount for calculation")

		 else:
		 	balance = amount - 8_350
		 	first_tax = (amount - amount + 8_350) * 0.10			
		 	
		 	if balance >= 0 and balance <= 8_350:
		 		total_tax = (balance * 0.10) + first_tax
		 		print("Tax payable is : " , total_tax)
			
		 	elif balance >= 8_351 and balance <= 33_950:

		 		total_tax = (balance * 0.15) + first_tax

		 		print("Tax payable is : ", total_tax)

		 	elif amount >= 33_951 and amount <= 82_250:
			
		 		total_tax = (balance * 0.25) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 82_251 and amount <= 171_550:
			
			 	total_tax = (balance * 0.28) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 171_551 and amount <= 372_950:
			
			 	total_tax = (balance * 0.33) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 372_951:
			
			 	total_tax = (balance * 0.35) + first_tax

		 		print("Tax payable is : ", total_tax)


	case 1 : 
		amount = float(input("Enter income amount: "))

		if amount < 0:

		 	print("Enter valid amount for calculation")

		else:
		 	balance = amount - 16_700
		 	first_tax = (amount - amount + 16_700) * 0.10			
		 	
		 	if balance >= 0 and balance <= 16_700:
		 		total_tax = (balance * 0.10) + first_tax
		 		print("Tax payable is : " , total_tax)
			
		 	elif balance >= 16_701 and balance <= 67_900:

		 		total_tax = (balance * 0.15) + first_tax

		 		print("Tax payable is : ", total_tax)

		 	elif amount >= 67_901 and amount <= 137_050:
			
		 		total_tax = (balance * 0.25) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 137_051 and amount <= 208_850:
			
			 	total_tax = (balance * 0.28) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 208_851 and amount <= 372_950:
			
			 	total_tax = (balance * 0.33) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 372_951:
			
			 	total_tax = (balance * 0.35) + first_tax

		 		print("Tax payable is f: ", total_tax)

	case 2 : 
		print("Calculation for Married filling separately")

		amount = float(input("Enter income amount: "))

		if amount < 0:

		 	print("Enter valid amount for calculation")

		else:
		 	balance = amount - 8_350
		 	first_tax = (amount - amount + 8_350) * 0.10			
		 	
		 	if balance >= 0 and balance <= 8_350:
		 		total_tax = (balance * 0.10) + first_tax
		 		print("Tax payable is : " , total_tax)
			
		 	elif balance >= 18_351 and balance <= 33_950:

		 		total_tax = (balance * 0.15) + first_tax

		 		print("Tax payable is : ", total_tax)

		 	elif amount >= 33_951 and amount <= 68_525:
			
		 		total_tax = (balance * 0.25) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 68_526 and amount <= 104_425:
			
			 	total_tax = (balance * 0.28) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 104_426 and amount <= 186_475:
			
			 	total_tax = (balance * 0.33) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 186_476:
			
			 	total_tax = (balance * 0.35) + first_tax

		 		print("Tax payable is f: ", total_tax)

	case 3 : 
		print("Head of Household")

		amount = float(input("Enter income amount: "))

		if amount < 0:

		 	print("Enter valid amount for calculation")

		else:
		 	balance = amount - 11_950
		 	first_tax = (amount - amount + 11_950) * 0.10			
		 	
		 	if balance >= 0 and balance <= 11_950:
		 		total_tax = (balance * 0.10) + first_tax
		 		print("Tax payable is : " , total_tax)
			
		 	elif balance >= 11_951 and balance <= 45_500:

		 		total_tax = (balance * 0.15) + first_tax

		 		print("Tax payable is : ", total_tax)

		 	elif amount >= 45_501 and amount <= 117_450:
			
		 		total_tax = (balance * 0.25) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 117_451 and amount <= 190_200:
			
			 	total_tax = (balance * 0.28) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 190_201 and amount <= 372_950:
			
			 	total_tax = (balance * 0.33) + first_tax

		 		print("Tax payable is : ", total_tax)


		 	elif amount >= 372_951:
			
			 	total_tax = (balance * 0.35) + first_tax

		 		print("Tax payable is f: ", total_tax)










				





