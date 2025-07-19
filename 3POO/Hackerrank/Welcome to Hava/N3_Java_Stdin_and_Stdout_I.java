import java.util.*;

public class N3_Java_Stdin_and_Stdout_I {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(), b = scan.nextInt(), c = scan.nextInt();
        scan.close();
        System.out.println(a); System.out.println(b); System.out.println(c);
    }
}