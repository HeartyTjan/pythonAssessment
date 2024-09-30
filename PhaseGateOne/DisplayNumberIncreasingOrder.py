print("""

	Display Number in Increasing Order
      ======================================
""")
print("You are required to enter three numbers")
print()

first_number = int(input("Enter a number : "))
second_number = int(input("Enter a number : "))
third_number = int(input("Enter a number : "))

largest = first_number
second_largest = 0
smallest = first_number

if (second_number > largest):
	second_largest = largest
	largest = second_number

else :
	if (second_number > second_largest):
		second_largest = second_number

if (third_number > largest):
	second_largest = largest
	largest = third_number
else :
	if (third_number > second_largest):
		second_largest = third_number

if (second_number < smallest):
	smallest = second_number

if (third_number < smallest):
	smallest = third_number

print(f" {smallest} {second_largest} {largest}")

	

