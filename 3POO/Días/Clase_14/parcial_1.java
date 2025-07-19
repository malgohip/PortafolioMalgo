import java.util.*;

public class parcial_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num=sc.nextInt(), den=sc.nextInt(); 
        sc.close();
        fraction frac=new fraction(num,den,num/den,num%den);
        frac.neg(); frac.printprop(); frac.printmxt();
    }
}