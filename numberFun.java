import java.util.Scanner;

public class numberFun {
    public static void main(String args[]){
        int num1, num2, num3, counter = 0;
        Scanner inp = new Scanner(System.in);
        int numTrials = inp.nextInt();
        while(counter < numTrials){
            num1 = inp.nextInt();
            num2 = inp.nextInt();
            num3 = inp.nextInt();
            if(num1 == num3+num2 || num2 == num1+num3 || num1+num2 == num3 || num1 == num2*num3 || num2 == num3*num1 || num3 == num1*num2){
                System.out.print("Possible");
            }
            else{
                System.out.print("Impossible");
            }
            counter += 1;
        }
    }
}
