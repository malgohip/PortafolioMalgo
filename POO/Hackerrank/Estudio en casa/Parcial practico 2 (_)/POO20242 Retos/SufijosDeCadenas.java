import java.util.*;

public class SufijosDeCadenas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palabra = sc.next(); System.out.println(palabra); int cont=0;
        while(cont<palabra.length()){cont++; System.out.println(palabra.substring(cont,palabra.length()));}
        sc.close();
    }
}
