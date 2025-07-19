import java.util.*;
import java.io.*;

public class N28Java1DArrayPart2{
   public static boolean canWin(int leap, int[] game) {
      boolean[] visited = new boolean[game.length];
      return canWinFrom(0, leap, game, visited);
   }

   private static boolean canWinFrom(int i, int leap, int[] game, boolean[] visited) {
      if (i >= game.length) return true; if (i < 0 || game[i] == 1 || visited[i]) return false; visited[i] = true;
      return canWinFrom(i - 1, leap, game, visited) || canWinFrom(i + 1, leap, game, visited) || canWinFrom(i + leap, leap, game, visited);
   }

   public static void main(String[] args) throws IOException{
      Scanner sc = new Scanner(new File("N28.txt"));
      int q = sc.nextInt();
      while (q-- > 0) {
         int n = sc.nextInt();
         int leap = sc.nextInt();
         int[] game = new int[n];
         for (int i = 0; i < n; i++) game[i] = sc.nextInt();
         System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
      }
      sc.close();
   }
}