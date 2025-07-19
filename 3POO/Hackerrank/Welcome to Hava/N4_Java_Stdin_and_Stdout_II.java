import java.util.*;

public class N4_Java_Stdin_and_Stdout_II {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(); double b = scan.nextDouble();
        scan.nextLine();  String c = scan.nextLine();
        scan.close();
        System.out.println("String: " + c); System.out.println("Double: " + b); System.out.println("Int: " + a);
    }
}