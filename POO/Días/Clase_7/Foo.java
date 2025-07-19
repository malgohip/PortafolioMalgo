public class Foo {
    public static final int CERO = 0;
    private static int contador = CERO;
    public int numero;
    public Foo(int numero){this.numero = numero; contador++;}
    public void print(){System.out.printf("numero=%d y contador=%d \n",numero,contador);}
    public static int getContador(){return contador;}

    public static void main(String[] args){
        System.out.println(Foo.getContador());
        Foo foo1, foo2; foo1=new Foo(5); foo2=new Foo(2);
        foo1.print(); foo2.print();
        System.out.println(Foo.getContador());
    }
}