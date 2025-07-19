import java.util.*;

public class RaicesCuadradas{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String datos = sc.nextLine(); datos+="\n"; ArrayList<Integer> numeros = separaNumeros(datos); 
        int a=numeros.get(0), b=numeros.get(1), c=numeros.get(2);
        double raiz = Math.sqrt(b*b-4*a*c), solucionA = (-b+raiz)/(2*a), solucionB = (-b-raiz)/(2*a);
        System.out.println(solucionA+" "+solucionB);
        sc.close();
    }

    static ArrayList<Integer> separaNumeros(String linea) {
        ArrayList<String> palabras = new ArrayList<String>(); String palabra = ""; ArrayList<Integer> numeros = new ArrayList<Integer>();
        for (int i=0; i<linea.length()-1; i++){char letra = linea.charAt(i); if(!(Character.isWhitespace(letra))) palabra+=letra; if (Character.isWhitespace(linea.charAt(i+1)) && !(palabra.equals(""))){palabras.add(palabra); palabra="";}}
        for (String s: palabras) numeros.add(Integer.valueOf(s)); return numeros;
    }
}