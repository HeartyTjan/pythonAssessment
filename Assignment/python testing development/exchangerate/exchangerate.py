
def get_exchange_rate(amount) :
	if amount < 0 :
		raise ValueError("Invalid amount. Enter amount") 
	EXCHANGE_RATE = 1550
	return  amount * EXCHANGE_RATE
