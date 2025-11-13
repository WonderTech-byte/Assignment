import java.util.Scanner;
public class AgeCheck {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

    System.out.print("Enter Fathers age: ");
    int fatherAge = input.nextInt();

    System.out.print("Enter Sons age: ");
    int sonsAge = input.nextInt();

    int yearsAgo = 2 * sonsAge - fatherAge;

    System.out.println("Answer: " + yearsAgo) ;   



    }
}
