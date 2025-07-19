import java.util.*;

public class Q1_Matriz_de_Fracciones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int N = sc.nextInt(); fraction[] fraciones = new fraction[N];
        for (int i=0; i<N; i++){
            int num = sc.nextInt(), den = sc.nextInt(); fraction frac=new fraction(num,den,num/den,num%den);
            frac.neg();
            fraciones[i] = frac;
        }
        int F = sc.nextInt(),  C = sc.nextInt(), cont=0; String c = sc.next();
        for (int i=0; i<F; i++){for (int j=0; j<C; j++){if (c.equals("p")) fraciones[cont].printprop(); else if (c.equals("m")) fraciones[cont].printmxt(); else if (c.equals("a")) {fraciones[cont].printprop(); fraciones[cont].printmxt();} cont+=1;} System.out.print("\n");}
        sc.close();
    }
}