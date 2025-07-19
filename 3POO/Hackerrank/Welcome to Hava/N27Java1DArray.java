import java.util.*;

public class N27Java1DArray{
   public static void main(String []args){
      Scanner sc = new Scanner(System.in); 
      int n = sc.nextInt(); int[] a = new int[n];
      for (int i=0; i<n; i++){int b = sc.nextInt(); a[i]=b;}
      sc.close();
      for (int j=0; j<n; j++){System.out.println(a[j]);}
   }
}