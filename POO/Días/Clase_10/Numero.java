public class Numero {
    int numero;
    public void set(int x){numero = x;}
    public int get(){return numero;}
    //public String toString(){return ""+numero;}
    public String toString(){return super.toString() + "--->" + numero;}
}
