import java.util.*;

public class solucion_quiz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num=sc.nextInt(), den=sc.nextInt(); 
        sc.close();
        Fraction f = new Fraction(num,den);
        System.out.println(f);
    }
}

class Fraction{
    public int nume,deno,cosi,resi;

    public Fraction(int num, int den){
        nume = num; deno = den;
        if (den < 0){ deno*=-1; nume*=-1;}
        cosi=Math.abs(num/den); resi=Math.abs(num%den);
    }

    public String propio(){ return nume+"/"+deno;}

    public String toString(){return cosi+propio();}
}

//En la clase siguiente terminamos
//Ya es la siguiente clase querido
//Y al final no hicieron nada, no mmgvasos