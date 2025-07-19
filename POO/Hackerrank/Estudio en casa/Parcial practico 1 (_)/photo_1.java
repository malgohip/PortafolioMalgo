import java.util.*;

public class photo_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt(); fraction[] fraciones = new fraction[n];
        for (int i=0;i<n;i++){int num=sc.nextInt(), den=sc.nextInt(); fraction frac=new fraction(num,den,num/den,num%den);fraciones[i]=frac;}
        char tprint = sc.next().charAt(0);
        sc.close();
        for (int i=0;i<fraciones.length;i++){
            fraciones[i].neg();
            if (tprint=='a'){fraciones[i].printprop(); System.out.print(" "); fraciones[i].printmxt(); System.out.print(" ");}
            else if (tprint=='m'){fraciones[i].printmxt(); System.out.print(" ");}
            else if (tprint=='p'){fraciones[i].printprop(); System.out.print(" ");}
        }
    }
}