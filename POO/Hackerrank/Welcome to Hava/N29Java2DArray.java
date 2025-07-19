import java.util.*; import java.io.*;

class relojDeArena{
   private int[] reloj = new int[7];
   public relojDeArena(int a, int b, int c, int d, int e, int f, int g){reloj[0]=a; reloj[1]=b; reloj[2]=c; reloj[3]=d; reloj[4]=e; reloj[5]=f; reloj[6]=g;}
   public String toString(){return reloj[0]+" "+reloj[1]+" "+reloj[2]+"\n  "+reloj[3]+"  \n"+reloj[4]+" "+reloj[5]+" "+reloj[6];}
   public int sum(){int suma=0; for (int i=0; i<reloj.length; i++) suma+=reloj[i]; return suma;}
}

public class N29Java2DArray{
   public static void main(String[] args) throws IOException{
      Scanner sc = new Scanner(new File("N29.txt")); int[][] matriz = new int[6][6];
      for (int i=0; i<6; i++) for (int j=0; j<6; j++) matriz[i][j]=sc.nextInt(); sc.close(); int max=-64;
      for (int i=0; i<4; i++)for (int j=0; j<4; j++){relojDeArena relojito = new relojDeArena(matriz[i][j], matriz[i][j+1], matriz[i][j+2], matriz[i+1][j+1], matriz[i+2][j], matriz[i+2][j+1], matriz[i+2][j+2]); if (max<relojito.sum()) max=relojito.sum();}
      System.out.println(max);
   }
}