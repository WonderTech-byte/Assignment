import java.util.Scanner;
public class Year {
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);

    System.out.print("Enter years in days: ");
    int year = input.nextInt();

    if(year % 4 == 0){
        System.out.println("its a leap year");
    }
       if(year % 100 == 0){        
            System.out.println("its not a leap year");
     
    }else if(year % 4 == 0 || year % 4 == 0|| year % 400 == 0){
        if(year % 100 == 0){        
                 System.out.println("its not a leap year");
            if(year % 400 == 0){
                System.out.println("its not a leap year");
             }
        }
    }
    
    }
}
