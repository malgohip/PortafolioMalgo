import java.util.*;

public class Q2_Arreglo_de_Tiempo{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cant=sc.nextInt();
        for (int i=0; i<cant; i++){
            sc.nextLine(); String nombre=sc.nextLine(); int precio=sc.nextInt(), cantidad=sc.nextInt();
            int agno=sc.nextInt(), mes=sc.nextInt(), dia=sc.nextInt(), hora=sc.nextInt(), minuto=sc.nextInt(), segundo=sc.nextInt(); String mediodia=sc.next(); time tiempo = new time(agno, mes, dia, hora, minuto, segundo, mediodia);
            compra comprita = new compra(nombre, precio, cantidad, tiempo); System.out.println(comprita); System.out.println();
        }
        sc.close();
    }
}