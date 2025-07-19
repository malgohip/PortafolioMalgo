import java.util.*;

class Punto{
    private long x,y;
    public long getX(){return x;} public long getY(){return y;}
    public void setCoord(String dire){String regex = "[\\s]";String[] Dir = dire.split(regex);this.x = Integer.parseInt(Dir[1]);this.y = Integer.parseInt(Dir[3]);}
    public Punto(){this.x=0; this.y=0;} public Punto(long x, long y){this.x=x;this.y=y;}
    public String toString(){return "("+x+","+y+")";}
    public double Distancia(Punto punto){return Math.sqrt(Math.pow(punto.y-y,2)+Math.pow(punto.x-x,2));}
    public double Distancia(){return Distancia(new Punto());}
}

public class Q4_Distancias{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        Punto prePuntos[]= new Punto[4];
        for (int i=0;i<4;i++){String dire=sc.nextLine(); if (formatoValido(dire)){Punto pun = new Punto(); pun.setCoord(dire); prePuntos[i]=pun;} else prePuntos[i]=null;}
        sc.close();
        ArrayList<Punto> lista = new ArrayList<>(); for (Punto punto : prePuntos) {if (punto != null) {lista.add(punto);}} Punto[] Puntos=lista.toArray(new Punto[0]);
        Punto a = Puntos[0]; Punto b = Puntos[1]; double distanciaMin = a.Distancia(b);
        for (int i=1;i<Puntos.length;i++){if (Puntos[0].Distancia(Puntos[(i)]) < distanciaMin){distanciaMin=Puntos[0].Distancia(Puntos[(i)]);b=Puntos[i];}}
        System.out.printf("Distancia m\u00e1s corta desde el punto inicial: %.3f%n", distanciaMin);
        double distanciaMax = a.Distancia(b);
        for (int i=0;i<(Puntos.length-1);i++){if (b.Distancia(Puntos[i+1]) > distanciaMax){distanciaMax=b.Distancia(Puntos[(i+1)]);}}
        System.out.printf("Distancia m\u00e1s larga desde el punto anterior: %.3f%n", distanciaMax);
        double distanciaT = distanciaMin + distanciaMax;
        System.out.printf("Distancia total: %.3f%n", distanciaT);
    }

    public static boolean formatoValido(String dire){
        String regex = "^carrera \\d+ # \\d+$";
        if (!dire.matches(regex)) return false;
        String[] partes = dire.split(" ");
        try {int numero1 = Integer.parseInt(partes[1]); int numero2 = Integer.parseInt(partes[3]); if (numero1 >= 0 && numero2 >= 0) return true;} catch (NumberFormatException e) {return false;}
        return false;
    }
}