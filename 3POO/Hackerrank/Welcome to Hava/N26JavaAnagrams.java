import java.util.*;

public class N26JavaAnagrams{
   public static void main(String []args){
      Scanner sc = new Scanner(System.in); String a = sc.next(), b=sc.next(); sc.close();
      if (isAnagram(a,b)) System.out.println("Anagrams"); else System.out.println("Not Anagrams");
   }

   static boolean isAnagram(String a, String b){
      a=a.toLowerCase(); HashMap<Character, Integer> dic_a = new HashMap<Character, Integer>();
      b=b.toLowerCase(); HashMap<Character, Integer> dic_b = new HashMap<Character, Integer>();
      for (int i=0; i<a.length(); i++){char j=a.charAt(i); if (dic_a.containsKey(j)) dic_a.replace(j, dic_a.get(j)+1); else dic_a.put(j,1);}
      for (int i=0; i<b.length(); i++){char j=b.charAt(i); if (dic_b.containsKey(j)) dic_b.replace(j, dic_b.get(j)+1); else dic_b.put(j,1);}
      return (dic_a.equals(dic_b));
   }
}