import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

    System.out.print("Enter Number ans operation to perform: ");
    int firstNum = input.nextInt();
    String operator = input.next();
    int secondNum = input.nextInt();
    
    if(operator.equals("+")){
        int sum = firstNum + secondNum;
        System.out.println("sum " +sum);
    }else if(operator.equals("*")){
        int product = firstNum * secondNum;
        System.out.println("product: " + product);
    }else if(operator.equals("/")){
        double quotient = firstNum / secondNum;
        System.out.println("product: " + quotient);
    }
    
    }
}
