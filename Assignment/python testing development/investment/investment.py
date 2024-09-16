def get_future_investment(amount,monthly_interest_rate,year):
	if amount < 0 or monthly_interest_rate < 0 or year < 0 :
		raise ValueError ("Invalid amount")

	if not isinstance(amount,(int,float)):
		raise TypeError("invalid input")

	if not isinstance(monthly_interest_rate, int):
		raise TypeError("invalid input")

	if not isinstance(year, int):
		raise TypeError("invalid input")

	MONTH_IN_YEAR = 12

	number_of_months = year * MONTH_IN_YEAR

	monthly_interest_rate = (monthly_interest_rate / 100) / MONTH_IN_YEAR

	future_investment = round(amount * (1 + monthly_interest_rate)** number_of_months,2)
	
	return future_investment


	