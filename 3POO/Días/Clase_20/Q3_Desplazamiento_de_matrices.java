import java.util.*;

public class Q3_Desplazamiento_de_matrices{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(); int[][] matriz = new int[N][M];
        int H = sc.nextInt(), V = sc.nextInt(); 
        for (int i = 0; i < N; i++){for (int j = 0; j < M; j++){ matriz[i][j] = sc.nextInt();}}
        matriz=desplazamientoHorizontalMatiz(matriz, H); matriz=desplazamientoVerticalMatiz(matriz, V);
        for (int i = 0; i < N; i++) {for (int j = 0; j < M; j++) System.out.print(matriz[i][j] + " "); System.out.print("\n");}
        sc.close();
    }

    static int[][] desplazamientoHorizontalMatiz(int[][] matriz, int H) {
        int N = matriz.length, M = matriz[0].length; int[][] desplazamientoMatriz = new int[N][M];
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) {if (j+H>=M) desplazamientoMatriz[i][j+H-M] = matriz[i][j]; else desplazamientoMatriz[i][j+H] = matriz[i][j];}
        return desplazamientoMatriz;
    }
    static int[][] desplazamientoVerticalMatiz(int[][] matriz, int V) {
        int N = matriz.length, M = matriz[0].length; int[][] desplazamientoMatriz = new int[N][M];
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) {if (i+V>=N) desplazamientoMatriz[i+V-N][j] = matriz[i][j]; else desplazamientoMatriz[i+V][j] = matriz[i][j];}
        return desplazamientoMatriz;
    }
}