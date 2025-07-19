import java.util.*;

public class N10_Java_Static_Initializer_Block {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int b = sc.nextInt() ,h = sc.nextInt(); sc.close();
        if (!(b<=0) && !(h<=0)) System.out.println(b*h);
        else System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}