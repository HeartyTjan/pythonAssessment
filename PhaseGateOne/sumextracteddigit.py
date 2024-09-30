integer = int(input("Enter number between 0 and 1000 : "))

first_digit = integer // 100
second_digit = integer // 10 % 10
third_digit = integer % 10

sum_of_digits = first_digit + second_digit + third_digit

print(f"Sum of extracted digit is : {sum_of_digits}")
