def get_future_days():

	future_days = int(input("Enter the number of days elapsed today : "))
	new_future_days =  day + future_days
	
	match new_future_days :
		
		case 0 : print("The Future day  is : Sunday")

		case 1 : print("The Future day  is : Monday")
	
		case 2 : print("The Future day  is : Tuesday")

		case 3 : print("The Future day  is : Wednesday")

		case 4 : print("The Future day  is : Thurday")

		case 5 : print("The Future day  is : Friday")
	
		case 6 : print("The Future day  is : Saturday")
		
		case _ : print("Enter a number from Sunday(0) - Saturday(6)")



day = int(input("Enter today's day : "))

match day :
		
	case 0 : 
		print("Today is : Sunday")
		get_future_days()
	case 1 : 
		print("Today is : Monday")
		get_future_days()
			 
	case 2 : 
		print("Today is : Tuesday")
		get_future_days()

	case 3 : 
		print("Today is : Wednesday")
		get_future_days()

	case 4 : 
		print("Today is : Thurday")
		get_future_days()


	case 5 : 
		print("Today is : Friday")
		get_future_days()
	
	case 6 : 
		print("Today is : Saturday")
		get_future_days()

	case _ : print("Enter a number from Sunday(0) - Saturday(6)")


