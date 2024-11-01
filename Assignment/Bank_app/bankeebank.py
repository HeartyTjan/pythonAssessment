import accountprocess

bank = []

choice = 1
while choice != 0:	

	print("""

	    Banke Bank Menu
	===============================

	 1 --> Open account 
	 2 --> Deposit money
	 3 --> Withdraw Money
	 4 --> Check account balance
	 5 --> Transfer 
	 6 --> Pin Modification
	 7 --> Close account
	 8 --> Check account number

       ==================================

		
	""")

	try:
		option = int(input("Enter your preferred option : "))

		match option :

			case 1 : 
				accountprocess.open_account()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 2 :
				accountprocess.deposit()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 3 :
				accountprocess.withdraw()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))
 

			case 4 :
				accountprocess.dispay_balance()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 5 :
				accountprocess.transfer()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 6 :
				print("""
				
					Pin Modification
				      =====================

					1 --> Change pin
					2 --> Check pin
				""")

				pin_option = int(input("Enter preferred option: "))
				
				match pin_option:
					
					case 1 :
						accountprocess.change_user_pin()
						choice = int(input("\nEnter 1 to continue or 0 to Quit : "))


					case 2 :
						accountprocess.check_user_pin()
						choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 7 :
				accountprocess.close_account()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

			case 8 :
				accountprocess.display_account_details()
				choice = int(input("\nEnter 1 to continue or 0 to Quit : "))

	except ValueError:
		print("Invalid input")

			
		
		