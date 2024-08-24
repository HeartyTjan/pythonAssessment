print("""
	
		Mortgage Calculator
	.................................
	"""
)


principal_amount = int(input("Enter principal Amount: "))

annual_Interest_Rate = int(input("Enter annual interest rate : "))
converted_annual_Interest_Rate = annual_Interest_Rate / 100
monthly_interest_rate = converted_annual_Interest_Rate / 12

duration_in_years = int(input("Enter duration in years : "))
duration_in_month = duration_in_years * 12

mortgage_calculation_1 = principal_amount * monthly_interest_rate * pow((1 + monthly_interest_rate), duration_in_month)
mortgage_calculation_2 = pow((1 + monthly_interest_rate), duration_in_month) - 1
mortgage_payment = mortgage_calculation_1 / mortgage_calculation_2

print("Monthly mortgage payment is : ${:,}".format(round(mortgage_payment,2)))

