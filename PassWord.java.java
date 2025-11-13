import java.util.Scanner;
public class PassWord{
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);

    System.out.print("Enter password: ");
    String password = input.nextLine();
    int length = password.length();

    System.out.println(length);
    }
}
