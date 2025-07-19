import java.util.*;

public class Subcadenas1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palabra = sc.next(); int cont_1=0;
        while(cont_1<palabra.length()){
            String sufijo=palabra.substring(cont_1,palabra.length()); System.out.println(sufijo); int cont_2=sufijo.length(); cont_1++; 
            while(cont_2>1){cont_2--; System.out.println(sufijo.substring(0,cont_2));}
        }
        sc.close();
    }
}
