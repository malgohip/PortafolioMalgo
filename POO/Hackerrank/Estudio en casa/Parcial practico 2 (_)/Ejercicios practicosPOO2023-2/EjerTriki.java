import java.util.*;

class triki{
    String[][] tablero = new String[3][3];
    triki(){for (int i=0; i<tablero.length; i++)for (int j=0; j<tablero[0].length; j++)tablero[i][j]="a";}
    public void marcarCasilla(String simbolo, int fila, int columna){tablero[fila][columna]=simbolo;}
    public String verificarCasilla(int fila, int columna){return tablero[fila][columna];}
    public String verificarGanador(){for (int i=0; i<tablero.length; i++) for (int j=0; j<tablero[0].length; j++){ if (i==0) if(tablero[0][j].equals(tablero[1][j]) && tablero[1][j].equals(tablero[2][j]) && tablero[0][j] != "a") return verificarCasilla(i, j); if (j==0) if(tablero[i][0].equals(tablero[i][1]) && tablero[i][1].equals(tablero[i][2]) && tablero[i][0] != "a") return verificarCasilla(i, j); if (i==0 && j==0) if(tablero[0][0].equals(tablero[1][1])&& tablero[1][1].equals(tablero[2][2]) && tablero[0][0] != "a") return verificarCasilla(i, j); if (i==0 && j==2) if (tablero[2][0].equals(tablero[1][1]) && tablero[1][1].equals(tablero[0][2]) && tablero[2][0] != "a") return verificarCasilla(i, j);}return "a";}
    public String imprimirTablero(){String concat=""; for (int i=0; i<tablero.length; i++){for (int j=0; j<tablero[0].length; j++) concat+=tablero[i][j]; concat+="\n";} return concat;}
}

public class EjerTriki{
    public static void main(String[] args) {
        triki partida = new triki(); Scanner sc = new Scanner(System.in);
        while (partida.verificarGanador()=="a"){
            String letra = sc.next(); 
            while (!(letra.equals("X")) && !(letra.equals("O"))){System.out.println("SNA"); letra = sc.next();}
            System.out.println("SA"); int fil = sc.nextInt(); int col = sc.nextInt();
            while ((fil>2 || col>2) || !(partida.verificarCasilla(fil, col).equals("a"))){System.out.println("CNA"); fil = sc.nextInt(); col = sc.nextInt();}
            System.out.println("CA"); partida.marcarCasilla(letra,fil,col);}
        System.out.print(partida.imprimirTablero()); System.out.println("El simbolo ganador fue: "+partida.verificarGanador()); sc.close();
    }
}