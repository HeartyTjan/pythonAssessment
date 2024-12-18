'''
	Request user for radius 
	Store value into radius
	initialize pi to be 3.142
	create a variable for area
	calculate pi * radius squared
	save the result into variable area.
	print area

	'''

radius = int(input("Enter radius : "))
name = input("Enter your name: ")
pi = 3.142
area = int(pi) * (radius ** 2)

print (pi)
print("The area of a circle using radius as ",radius,"is", round(area, 2))
print ("Thank you", name, " for calculating the area")