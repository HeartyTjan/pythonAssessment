count = 9
for i in range(1,11):
	print(f" {(11-i) * "*"} {3 * " "}  {i * "*"} {2 * " "} {(i + count) * "*"}   {2 * " "} {" " * (10-i) + i * "*" }  ")

	count -= 2  