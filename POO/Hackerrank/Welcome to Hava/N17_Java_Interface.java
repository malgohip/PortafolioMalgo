import java.util.*;

interface AdvancedArithmetic{
    int divisor_sum(int n);
}

class MyCalculator implements AdvancedArithmetic{
    public int divisor_sum(int n){int sum=0; for (int i=1;i<=n;i++){if ((n%i)==0) sum+=i;} return sum;}
}

public class N17_Java_Interface {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); int N = sc.nextInt(); sc.close();
        MyCalculator j = new MyCalculator(); System.out.println("I implemented: AdvancedArithmetic"); System.out.println(j.divisor_sum(N));
    }
}