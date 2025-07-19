public class Clase26 {

    public int calcular(int a, int b, opBin oper){
        return oper.op(a,b);
    }

    public static void main(String[] args) {
        Clase26 calcul = new Clase26();
        System.out.println(calcul.calcular(4,3,(a,b)->a+b));
        System.out.println(calcul.calcular(7,4,(a,b)->a-b));
        System.out.println(calcul.calcular(4,7,(a,b)->a*b));
        System.out.println(calcul.calcular(20,4,new Div()));
        System.out.println(calcul.calcular(20,17,new opBin(){
            public int op(int a, int b){
                return a%b;
            }
        }));
    }
}

interface opBin{
    public int op(int a, int b);
}

class Div implements opBin{
    public int op(int a, int b){
        return a/b;
    }
}