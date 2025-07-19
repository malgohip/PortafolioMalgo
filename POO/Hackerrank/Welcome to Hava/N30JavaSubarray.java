import java.util.*; import java.io.*;

public class N30JavaSubarray{
   public static void main(String[] args) throws IOException{
      Scanner sc = new Scanner(new File("N30.txt"));
      int n = sc.nextInt(); int[] serie = new int[n];
      for (int i=0; i<n; i++) serie[i]=sc.nextInt(); sc.close(); ArrayList<ArrayList<Integer>> partes = new ArrayList<>(); 
      for (int i=0; i<n; i++) for (int j=i; j<n; j++){ArrayList<Integer> parte = new ArrayList<>(); for (int k=i; k<j+1; k++){parte.add(serie[k]);} partes.add(parte);} ArrayList<Integer> sumas = new ArrayList<>(); 
      for (int i=0; i<partes.size(); i++){int suma=0; for (int j=0; j<partes.get(i).size(); j++){suma+=partes.get(i).get(j);} sumas.add(suma);} int cont=0;
      for (int i=0; i<sumas.size(); i++){if (sumas.get(i)<0) cont++;}
      System.out.println(cont);
   }
}