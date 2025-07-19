import java.util.*;

public class PrefijosDeCadenas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palabra = sc.next(); System.out.println(palabra); int cont=palabra.length();
        while(cont>0){cont--; palabra=palabra.substring(0, cont); System.out.println(palabra);}
        sc.close();
    }
}
