import java.util.*;

public class Q2_Rotacion_de_Matrices_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt(), N = sc.nextInt(), M = sc.nextInt(); int[][] matriz = new int[N][M];
        for (int i = 0; i < N; i++){ for (int j = 0; j < M; j++){ matriz[i][j] = sc.nextInt();}} sc.close();
        for (int x = 0; x < R; x++) matriz=rotacionMatriz(matriz);
        for (int[] fila : matriz) { for (int valor : fila) System.out.print(valor + " "); System.out.print("\n");}
    }

    static int[][] rotacionMatriz(int[][] matriz) {
        int N = matriz.length, M = matriz[0].length; int[][] rotacionMatriz = new int[M][N];
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) rotacionMatriz[M-1-j][i] = matriz[i][j];
        return rotacionMatriz;
    }
}