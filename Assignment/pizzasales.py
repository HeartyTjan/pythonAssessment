def calculate_sapa_size(number_of_people) :
	sapa_size = 4
	PRICE = 2000 
	
	number_of_boxes = number_of_people / sapa_size
	reminder = number_of_people % sapa_size
	if reminder == 0 :
		print("Number of boxes of pizza to buy = " , number_of_boxes, " boxes")
		print("Price = " , number_of_boxes * PRICE , "\n\n")
	else :
		accurate_number_of_boxes = number_of_boxes + 1;
		pizza_slice_reminder = (accurate_number_of_boxes * sapa_size) - number_of_people

		print("Number of boxes of pizza to buy = " , accurate_number_of_boxes, " boxes")
		print("Number left over slice after serving = " , pizza_slice_reminder, " slices")
		print("Price = " , accurate_number_of_boxes * PRICE,"\n\n")
	
	print("Thank you for patronizing Iya Afeez Pizza Joint")

def calculate_small_money(number_of_people) :
	small_money = 6
	PRICE = 2400

	number_of_boxes = number_of_people / small_money
	reminder = number_of_people % small_money
	if reminder == 0 :

		print("Number of boxes of pizza to buy = " , number_of_boxes, " boxes")
		print("Price = " , number_of_boxes * PRICE , "\n\n")

	else :
		accurate_number_of_boxes = number_of_boxes + 1;
		pizza_slice_reminder = (accurate_number_of_boxes * small_money) - number_of_people

		print("Number of boxes of pizza to buy = " , accurate_number_of_boxes, " boxes")
		print("Number left over slice after serving = " , pizza_slice_reminder, " slices")
		print("Price = " , accurate_number_of_boxes * PRICE , "\n\n")
	
	print("Thank you for patronizing Iya Afeez Pizza Joint")

def calculate_big_boys(number_of_people) :
	big_boys = 8
	PRICE = 3000

	number_of_boxes = number_of_people / big_boys
	reminder = number_of_people % big_boys
	if reminder == 0 :
	 
		print("Number of boxes of pizza to buy = " , number_of_boxes, " boxes")
		print("Price = " , number_of_boxes * PRICE, "\n\n")
	else :
		accurate_number_of_boxes = number_of_boxes + 1;
		pizza_slice_reminder = (accurate_number_of_boxes * big_boys) - number_of_people
		
		print("Number of boxes of pizza to buy = " , accurate_number_of_boxes, " boxes")
		print("Number left over slice after serving = " , pizza_slice_reminder, " slices")
		print("Price = " , accurate_number_of_boxes * PRICE , "\n\n")
	
	print("Thank you for patronizing Iya Afeez Pizza Joint")

def calculate_odogwu(number_of_people) :
	odogwu = 12
	PRICE = 4200

	number_of_boxes = number_of_people / odogwu
	reminder = number_of_people % odogwu
	if reminder == 0 :
		print("Number of boxes of pizza to buy = " , number_of_boxes, " boxes")
		print("Price = " , number_of_boxes * PRICE , "\n\n")
	else :
		accurate_number_of_boxes = number_of_boxes + 1;
		pizza_slice_reminder = (accurate_number_of_boxes * odogwu) - number_of_people

		print("Number of boxes of pizza to buy = " , accurate_number_of_boxes, " boxes")
		print("Number left over slice after serving = " , pizza_slice_reminder, " slices")
		print("Price = " , accurate_number_of_boxes * PRICE , "\n\n")
	
	print("Thank you for patronizing Iya Afeez Pizza Joint")


def displayPizzaTypeMenu() :
	print("""

         Pizza type Menu and Prices
  -----------------------------------------------------------
  | S/N |Pizza Type 	| Number of Slices | Price per box  |
  |-----|--------------	|------------------|----------------|
  |  1  |Sapa size	| 4  		   |  2,000	    |
  |-----|--------------	|------------------|----------------|
  |  2  |Small Money	| 6		   |  2,400	    |
  |-----|--------------	|------------------|----------------|
  |  3  |Big boys   	| 8		   |  3,000         |
  |-----|--------------	|------------------|----------------|
  |  4  |Odogwu	    	| 12               |  4,200         |
  -----------------------------------------------------------
    """
  )

displayPizzaTypeMenu()
pizzaTypeMenu = int(input("Enter preferred option: "))
match pizzaTypeMenu :
	case 1 : 
		number_of_people = int(input("Your preferred pizza type : Sapa Size\nEnter Number of people : "))
		print("")
		calculate_sapa_size(number_of_people)

	case 2 :
		number_of_people = int(input("Your preferred pizza type : Small Money\nEnter Number of people : "))
		print("")
		calculate_small_money(number_of_people)

	case 3 :
		number_of_people = int(input("Your preferred pizza type : Big Boys\nEnter Number of people : "))
		print("")
		calculate_big_boys(number_of_people)
	
	case 4 :
		number_of_people = int(input("Your preferred pizza type : Sapa size\nEnter Number of people : "))
		print("")
		calculate_odogwu(number_of_people)
		