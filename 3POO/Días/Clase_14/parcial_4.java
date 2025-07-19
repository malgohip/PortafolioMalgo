import java.util.*;

public class parcial_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int n=sc.nextInt(); fraction[] fraciones = new fraction[n];
        for (int i=0;i<n;i++){int num=sc.nextInt(), den=sc.nextInt(); fraction frac=new fraction(num,den,num/den,num%den);fraciones[i]=frac;}
        int num=sc.nextInt(), den=sc.nextInt(); fraction x = new fraction(num,den,num/den,num%den); sc.close(); 
        fraction dif = fraciones[0].diference(x); int indexf = 0; float difp =Math.abs((float) dif.num)/Math.abs((float)dif.den);
        for (int i=1;i<fraciones.length;i++){
            fraction difi=fraciones[i].diference(x); float difip =Math.abs((float) difi.num)/Math.abs((float)difi.den);
            if (difip<difp) {indexf=i; dif=difi; difp =Math.abs((float) dif.num)/Math.abs((float)dif.den);}
        }
        dif.neg(); dif.printmxt(); System.out.print("\n"); fraciones[indexf].printmxt();
    }
}
