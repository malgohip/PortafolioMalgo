public class PuntoD {
    private double x,y;

    public PuntoD(){
        //x=0;   y=0;
        this(0,0);
    }

    public PuntoD(double x1, double y1){
        x=x1;   y=y1;
    }
    
    public PuntoD(PuntoD p){
        //x=p.x;  y=p.y;
        this(p.x,p.y);
    }

    public void print(){
        System.out.println("("+x+","+y+")");
    }

    public double distancia(PuntoD punto){
        return Math.sqrt(Math.pow(punto.y-y,2)+Math.pow(punto.x-x,2));
    }

    public double distancia(){ //distancia al origen
        //return Math.sqrt(x*x+y*y);
        return distancia(new PuntoD());
    }

    public PuntoD puntoMedio(PuntoD punto){
        return new PuntoD((x+ punto.x)/2,(x+ punto.y)/2);
    }

    public static void main(String[] args){
        PuntoD a = new PuntoD(), b = new PuntoD(a);
        a.print(); b.print(); a.puntoMedio(b).print();
        System.out.println(a.distancia(b)); System.out.println(a.distancia());
    }
}
