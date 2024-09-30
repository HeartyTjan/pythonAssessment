import java.util.Scanner;
public class SumExtractedDigits{

	public static void main(String... args){

		Scanner receiver = new Scanner(System.in);

		System.out.print("Enter number between 0 and 1000 : ");
		int integer = receiver.nextInt();

		int first_digit = integer / 100;
		int second_digit = integer / 10 % 10;
		int third_digit = integer % 10;

		int sum_of_digits = first_digit + second_digit + third_digit;
		
		System.out.printf("Sum of extracted digit is : %d ", sum_of_digits);


	}

}