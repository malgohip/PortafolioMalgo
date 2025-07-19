import java.util.*;
import java.io.*;

public class N21JavaIterator{
   static Iterator<Object> func(ArrayList<Object> mylist){
      Iterator<Object> it=mylist.iterator();
      while(it.hasNext()){
         Object element = it.next();
         if((element instanceof Integer)||((element.equals("###")))) it.remove();
      }
      it=mylist.iterator();
      return it;
   }
   public static void main(String []args) throws IOException {
      ArrayList<Object> mylist = new ArrayList<Object>();
      Scanner sc = new Scanner(new File("N21.txt"));
      int n = sc.nextInt();
      int m = sc.nextInt();
      for(int i = 0;i<n;i++){
         mylist.add(sc.nextInt());
      }
      
      mylist.add("###");
      for(int i=0;i<m;i++){
         mylist.add(sc.next());
      }
      
      Iterator<Object> it=func(mylist);
      while(it.hasNext()){
         Object element = it.next();
         System.out.println(element);
      }
      sc.close();
   }
}