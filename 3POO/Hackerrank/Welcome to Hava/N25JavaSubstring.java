import java.util.*;

public class N25JavaSubstring{
   public static void main(String []args){
      Scanner sc = new Scanner(System.in); String s = sc.next(); int i = sc.nextInt(), e=sc.nextInt(); sc.close();
      System.out.println(s.substring(i,e-1));
   }
}