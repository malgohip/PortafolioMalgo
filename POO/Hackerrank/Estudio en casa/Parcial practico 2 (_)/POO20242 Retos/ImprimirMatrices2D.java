import java.util.*;

public class ImprimirMatrices2D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(); int[][] matriz = new int[N][M];
        for (int i = 0; i < N; i++){for (int j = 0; j < M; j++){ matriz[i][j] = sc.nextInt();}}
        for (int i = 0; i < N; i++) {for (int j = 0; j < M; j++) System.out.print(matriz[i][j] + " "); System.out.print("\n");}
        sc.close();
    }
}
