winning = ["31","15","61"]

name = input("Enter name :")
number = input("Enter number : ")

number = number.split(" ")

if number[0] == winning[0] and number[1] == winning[1] and number[2] == winning[2]:
	print(f"You won $ {5000 :,d}")

elif number[0] == winning[1] and number[1] == winning[2] and number[2] == winning[0]:
	print(f"You won $ {4000 :,d}")

elif number[0] == winning[2] and number[1] == winning[1] and number[2] == winning[0]:
	print(f"You won $ {4000 :,d}")

elif number[0] == winning[1] and number[1] == winning[0] and number[2] == winning[2]:
	print(f"You won $ {4000 :,d}")

elif number[0] == winning[2] and number[1] == winning[0] and number[2] == winning[1]:
	print(f"You won $ {4000 :,d}")

elif number[0] == winning[0] and number[1] == winning[2] and number[2] == winning[1]:
	print(f"You won $ {4000 :,d}")

elif number[0] == winning[0] and number[1] == winning[2] and number[2] == winning[1]:
	print(f"You won $ {4000 :,d}")

if number[0] == winning[1] and number[2] == winning[2] or number[1] == winning[1] and number[2] == winning[2]:
	print(f"You won $ {3000 :,d}")

elif number[0] == winning[1] and number[1] == winning[2] :
	print(f"You won $ {3000 :,d}")

elif number[0] == winning[1] or number[1] == winning[2] or number[0] == winning[2] or number[1] == winning[1]:
	print(f"You won $ {2000 :,d}")

elif number[2] == winning[1] or number[2] == winning[2] or number[2] == winning[0] or number[0] == winning[0]:
	print(f"You won $ {2000 :,d}")

elif number[1] == winning[0] or number[2] == winning[2] or number[2] == winning[0] or number[0] == winning[0]:
	print(f"You won $ {2000 :,d}")

else :
	print(f"Try again {name} ")