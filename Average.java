import java.util.Scanner;
public class Average {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

     System.out.print("Enter first score: ");
     int firstScore = input.nextInt();
    
    System.out.print("Enter second Score: ");
    int secondScore = input.nextInt();

    System.out.print("Enter third Score: ");
    int thirdScore = input.nextInt();

    int average = (firstScore + secondScore + thirdScore)/ 3;
    if(average <= 60){
        System.out.println("GRADE--F");
    }else if(average > 60 && average <= 70){
        System.out.println("GRADE --D");
    }else if(average > 70 && average <= 80){
        System.out.println("GRADE---C");
    }else if(average > 80 && average <= 90){
        System.out.println("GRADE---B");
    }else if(average > 90 && average <= 100){
        System.out.println("GRADE--A");
    }
    
    }
}


