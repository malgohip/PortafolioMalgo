import java.util.Scanner;

public class Clase_18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt(), d=sc.nextInt();
        System.out.println(new fraction(n,d)+" "+new mixed(n,d));
        sc.close();
    }
}