import java.util.*;

public class N2_Java_If_Else {
  private static final Scanner sc = new Scanner(System.in);
  public static void main(String[] args){
      int N = sc.nextInt(); sc.skip("(\r\n|[\n\r\u2028\u2029\u0085])?"); sc.close();
      if (N%2 == 1) System.out.println("Weird");
      else if (N <= 5) System.out.println("Not Weird");
      else if (N <= 20) System.out.println("Weird");
      else System.out.println("Not Weird");
  }
}