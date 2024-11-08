print('''

	Investment Return
       ====================
''')


def get_investment_roi(amount,years,percentage):

	if not isinstance (amount,(int,float)):

		raise ValueError("Invalid input")

	if amount < 0 or years < 0 or percentage < 0:

		raise ("Enter a valid amount, please.")
	
		percenatge_decimal = percentage / 100

		print(f" year\tinterest\ttotal amount")

		for year in range(1,years+1) :

			interest = amount * percenatge_decimal
			annual_return = amount + interest
			amount = annual_return

			print(f" {year} \t{round(interest,2)} \t {round(annual_return,2)}")




amount = float(input("Enter amount : "))
years = int(input("Enter year : "))
percentage = int(input("Enter rate in as integer : "))

print(get_investment_roi(amount,years,percentage))
print(get_investment_roi(1000000,10,10))