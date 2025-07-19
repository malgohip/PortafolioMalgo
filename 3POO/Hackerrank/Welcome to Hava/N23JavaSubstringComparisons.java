import java.util.*;

public class N23JavaSubstringComparisons{

   public static void main(String []args){
      Scanner sc = new Scanner(System.in); String s = sc.next(); int k=sc.nextInt(); sc.close(); ArrayList<String> Substrings = new ArrayList<String>();
      for (int i=0; i<s.length(); i++){if (i+k<s.length()+1){String sub = s.substring(i, i+k); Substrings.add(sub);} }
      String min="zzz", max="AAA";
      for (int i=0; i<Substrings.size(); i++){if (Substrings.get(i).compareTo(min)<=0) min=Substrings.get(i); if (Substrings.get(i).compareTo(max)>0) max=Substrings.get(i);}
      System.out.println(min+"\n"+max);
   }
}