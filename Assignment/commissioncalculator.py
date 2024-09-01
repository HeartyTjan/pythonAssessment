def calculate_commission(collection_rate) :
	
	basePay = 5000;

	if collection_rate < 50 : 
		print("Rider payment for the day : {:,}" .format((collection_rate * 160) + 5000))	

	if collection_rate >= 50 and collection_rate <= 59 :
		print("Rider payment for the day : {:,}" .format((collection_rate * 200) + 5000))

	if collection_rate >= 60 and collection_rate <= 69 :
		print("Rider payment for the day : {:,}" .format((collection_rate * 250) + 5000))

	if collection_rate >= 70 :
 		print("Rider payment for the day : {:,}" .format((collection_rate * 500) + 5000))

print("""
			
	Commission Calculator
------------------------------------
""")

successful_delivery = int(input("Enter rider collection Rate for the day : "))

calculate_commission(successful_delivery)