gallon_used = int(input("Enter the gallon used : "))

total_gallon = 0
total_miles = 0

while gallon_used != -1 :
	
	total_gallon += gallon_used

	miles_driven = int(input("Enter the miles driven : "))
	total_miles += miles_driven

	print("miles per gallon for each trip" , round(miles_driven / gallon_used,2))
	print()

	gallon_used = int(input("Enter the gallon used (-1 to end): "))

print()
print("miles per gallon for total trip" , round(total_miles / total_gallon,2))