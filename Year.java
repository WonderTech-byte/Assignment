import java.util.Scanner;
public class Year {
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);

    System.out.print("Enter years in days: ");
    int year = input.nextInt();

    if(year % 2 == 0 || year % 400 == 0){
        System.out.println("its a leap year");
    }else{
        System.out.println("ita not a leap year");
    }
    
    }
}
