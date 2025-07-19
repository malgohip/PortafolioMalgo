import java.util.*;

public class Q1_Clase_Tiempo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int agno=sc.nextInt(), mes=sc.nextInt(), dia=sc.nextInt(), hora=sc.nextInt(), minuto=sc.nextInt(), segundo=sc.nextInt(); String mediodia=sc.next();
        time tiempo = new time(agno, mes, dia, hora, minuto, segundo, mediodia); System.out.println(tiempo); 
        sc.close();
    }
}