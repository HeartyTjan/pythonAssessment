import java.util.Scanner;
public class DisplayNumberIncreasingOrder{

	public static void main(String... args){

		Scanner receiver = new Scanner(System.in);
	
		System.out.print("""
				Display Number in Increasing Order
				======================================

		You are required to enter three numbers

		""");

		System.out.print("Enter a number : ");
		int first_number = receiver.nextInt();

		System.out.print("Enter a number : ");
		int second_number = receiver.nextInt();

		System.out.print("Enter a number : ");
		int third_number = receiver.nextInt();

		int largest = first_number;
		int second_largest = 0;
		int smallest = first_number;

		if (second_number > largest){
	
			second_largest = largest;
			largest = second_number;
		}

		else {
			if (second_number > second_largest) second_largest = second_number;

		}

		if (third_number > largest){
			second_largest = largest;
			largest = third_number;
		}
		else {
			if (third_number > second_largest) second_largest = third_number;
		}

		if (second_number < smallest) smallest = second_number;

		if (third_number < smallest) smallest = third_number;

		System.out.printf("Output in increasing order : %d %d %d", smallest, second_largest, largest);

	}







}








	
