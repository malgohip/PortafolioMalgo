import java.util.*;
 
class PuntoD{
    public int x,y;
    public PuntoD(){this(0,0);}
    public PuntoD(int x1, int y1){x=x1;   y=y1;}
    public PuntoD(PuntoD p){this(p.x,p.y);}
    public void print(){System.out.println(x+" "+y);}
    public double Distancia(PuntoD punto){return Math.sqrt(Math.pow(punto.y-y,2)+Math.pow(punto.x-x,2));}
    public double Distancia(){return Distancia(new PuntoD());}
}

public class DistanciasEntrePuntosEn2Dimensiones1{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n=sc.nextInt(); PuntoD[] punto = new PuntoD[n];
        for (int i=0;i<n;i++){ int x=sc.nextInt(), y=sc.nextInt(); punto[i]=new PuntoD(x,y);}
        sc.close();
        PuntoD a = punto[0]; PuntoD b = punto[1]; double distanciaMin = a.Distancia(b);
        for (int i=0;i<n;i++){for (int j=i+1;j<n;j++){if (punto[i].Distancia(punto[j]) < distanciaMin) {distanciaMin=punto[i].Distancia(punto[j]);a=punto[i];b=punto[j];}}}
        System.out.printf("%.1f%n", distanciaMin); a.print(); b.print();
    }
}