import java.util.*;

public class N24JavaStringReverse{
   public static void main(String []args){
      Scanner sc = new Scanner(System.in); String s = sc.next(); sc.close(); String as = reverser(s);
      if (s.equals(as)) System.out.println("Yes"); else System.out.println("No");
   }

   static String reverser(String s){
      String as = ""; for (int i = s.length()-1; 0<=i; i--){as+=s.charAt(i);} return as;
   }
}