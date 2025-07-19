import java.util.*;

public class SumaDeStrings{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String linea = sc.nextLine(); linea+="j"; ArrayList<String> numeros = separaNumeros(linea); int numero = 0;
        for (String p: numeros) numero+=Integer.valueOf(p); System.out.println(numero);
        sc.close();
    }

    static ArrayList<String> separaNumeros(String linea) {
        ArrayList<String> numeros = new ArrayList<String>(); String numero_str = "";
        for (int i=0; i<linea.length()-1; i++){char letra = linea.charAt(i); if (Character.isDigit(letra)) numero_str+=letra; if (!(Character.isDigit(linea.charAt(i+1))) && !(numero_str.equals(""))){ numeros.add(numero_str); numero_str="";}}
        return numeros;
    }
}