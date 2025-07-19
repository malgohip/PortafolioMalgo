import java.util.*;

public class parcial_3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt(); fraction[] fraciones = new fraction[n];
        for (int i=0;i<n;i++){int num=sc.nextInt(), den=sc.nextInt(); fraction frac=new fraction(num,den,num/den,num%den);fraciones[i]=frac;}
        sc.close();
        for (int i=0;i<(fraciones.length-1);i++){
            fraction divi=fraciones[i].division(fraciones[i+1]);
            divi.neg();
            divi.printmxt(); System.out.print(" ");
        }
    }
}