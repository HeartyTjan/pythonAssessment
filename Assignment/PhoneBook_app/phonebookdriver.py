import contacts


def display_edit_menu():

	print("""

		  Edit Menu
	  =======================

	   1 --> Edit first name
		
	   2 --> Edit last name

	   3 --> Edit phone number

	 =========================
	""")	

def display():


	choice = 1

	while choice != 0 :

		print("""

	     	  PhoneBook App Menu
    	=======================================

          1 --> Add contact

	  2 --> Edit contact
	
	  3 --> Find contact via first name

	  4 --> Find contact via phone number
	
	  5 --> Delete contact

     	========================================
	""")

		try :
			option = int(input("Enter an preferred option : "))
	
			match option :
	
				case 1 : 
					contacts.add_contact()
					choice = int(input("Enter 1 to continue or 0 to quit : "))

				case 2 : 
					display_edit_menu()
					
					edit_option = int(input("Enter an preferred option : "))

					match edit_option :

						case 1 :
							contacts.edit_first_name()
							choice = int(input("\nEnter 1 to continue or 0 to quit : "))

						case 2 : 
							contacts.edit_last_name()
							choice = int(input("\nEnter 1 to continue or 0 to quit : "))

						case 3 :
							contacts.edit_phone_number()
							choice = int(input("\nEnter 1 to continue or 0 to quit : "))

				case 3 :
					contacts.find_contact_first_name()
					choice = int(input("\nEnter 1 to continue or 0 to quit : "))

				case 4 :
					contacts.find_contact_phone_number()
					choice = int(input("\nEnter 1 to continue or 0 to quit : "))		

				case 5 :
					contacts.remove_contact()
					choice = int(input("\nEnter 1 to continue or 0 to quit : "))

				case _ :
					print("\nEnter a valid option")
		

		except ValueError:	
			print("\nInvalid Input")


display()