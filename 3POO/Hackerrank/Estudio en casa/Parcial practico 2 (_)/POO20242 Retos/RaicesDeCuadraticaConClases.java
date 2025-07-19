import java.util.*;

class cuadratica{
    int a, b, c;
    public cuadratica(){this(1,0,-1);}
    public cuadratica(int A, int B, int C){a=A; b=B; c=C;}
    public void respuestas(){double raiz = Math.sqrt(b*b-4*a*c), solucionA = (-b+raiz)/(2*a), solucionB = (-b-raiz)/(2*a); System.out.println(solucionA+" "+solucionB);}
}

public class RaicesDeCuadraticaConClases{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.nextLine(); int a = separaNumerosRaro(A); 
        String B = sc.nextLine(); int b = separaNumerosRaro(B); 
        String C = sc.nextLine(); int c = separaNumerosRaro(C); 
        if (a==0) System.out.println("a cannot be zero");
        else if (b*b < 4*a*c) System.out.println("b squared is less than 4ac");
        else {cuadratica cuat = new cuadratica(a,b,c); cuat.respuestas();}
        sc.close();
    }

    static int separaNumerosRaro(String linea) {
        String util = linea.substring(2); return Integer.valueOf(util);
    }
}