import java.util.*;

public class ConcatenacionDeLenguajes{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String lenguaje_a = sc.nextLine(); lenguaje_a+="\n"; ArrayList<String> lenguaje_A = separaPalabras(lenguaje_a); 
        String lenguaje_b = sc.nextLine(); lenguaje_b+="\n"; ArrayList<String> lenguaje_B = separaPalabras(lenguaje_b); 
        String concat = ""; for (String a: lenguaje_A) for (String b: lenguaje_B) concat+=a+b+" "; System.out.println(concat);
        sc.close();
    }

    static ArrayList<String> separaPalabras(String linea) {
        ArrayList<String> palabras = new ArrayList<String>(); String palabra = "";
        for (int i=0; i<linea.length()-1; i++){
            char letra = linea.charAt(i); if(Character.isLetter(letra)) palabra+=letra; if (Character.isWhitespace(linea.charAt(i+1)) && !(palabra.equals(""))){palabras.add(palabra); palabra="";}}
        return palabras;
    }
}