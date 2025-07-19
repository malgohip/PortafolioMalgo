public class Clase_19 {
    public static void main(String[] args) {
        PolyReg[] reg = new PolyReg[4];
        reg[0]=new Triangulo(5);
        reg[1]=new Cuadrado(5);
        reg[2]=new Hexagono(5);
        reg[3]=new Octagono(5);
        for (PolyReg r: reg) System.out.println(r.area());
    }
}

abstract class PolyReg{
    protected int lado;
    protected PolyReg(int l){lado=l;}
    protected double area(){return lado*lado;}
}

class Triangulo extends PolyReg{
    public Triangulo(int lado){super(lado);}
    public double area(){return Math.sqrt(3)/4*super.area();}
}

class Cuadrado extends PolyReg{
    public Cuadrado(int lado){super(lado);}
}

class Hexagono extends PolyReg{
    public Hexagono(int lado){super(lado);}
    public double area(){return 3*Math.sqrt(3)/2*super.area();}
}

class Octagono extends PolyReg{
    public Octagono(int lado){super(lado);}
    public double area(){return 2*(1+Math.sqrt(2))*super.area();}
}