import java.util.*;

public class N11_Java_Int_to_String {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(); String s = "" + n; sc.close();
        if (s instanceof String) System.out.println("Good job"); else System.out.println("Wrong answer");
    }
}