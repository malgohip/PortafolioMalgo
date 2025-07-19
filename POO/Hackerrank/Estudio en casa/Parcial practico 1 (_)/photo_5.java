import java.util.*;

public class photo_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt(); fraction[] fraciones = new fraction[n];
        for (int i=0;i<n;i++){int num=sc.nextInt(), den=sc.nextInt(); fraction frac=new fraction(num,den,num/den,num%den);fraciones[i]=frac;}
        sc.close();
        fraction suma = new fraction();
        for (int i=0;i<fraciones.length;i++){
            fraciones[i].simplfier().printprop(); 
            suma=suma.addition(fraciones[i]);
        }
        suma.simplfier(); suma.printprop();
    }
}