public class Clase_8 {
    public static void main (String[] args){
        /*String x = new String("Hola, mundo");
        x = x + "!";
        String y = "Hola, mundo!";
        String z =x + y;
        System.out.println("x: " + x);
        System.out.println("x==y: " + (x==y));
        System.out.println("y==z: " + (y==z));
        System.out.println("x==z: " + (x==z));*/

        /*int num1, num2;
        String str1, str2;
        num1 = 2;
        num2 = 3;
        str1 = new String("num1 + num2 = ");
        str2 = new String(" = num1 + num2");
        System.out.println(str1+num1+num2);
        System.out.println(num1+num2+str2);*/

        /*String s=null;
        String t="";
        //int lenghts=s.length(); //NullPointerException 
        int lenghtt=t.length();
        System.out.println("s: " + s + "\nlength: " + /*lenghts "NullPointerException.");
        System.out.println("t: " + t + "\nlength: " + lenghtt);*/

        Ref ref = new Ref(), r2 = new Ref(); ref.setRef(r2); //r2.setRef(ref); Bucle de referencias
        System.out.println(ref); System.out.println(r2);
        //System.out.println(ref.getRef()); System.out.println(r2.getRef()); 

        /*System.out.println(new String ("UNAL")==new String ("UNAL"));
        System.out.println("UNAL".substring(0,2));*/

        /*String str3, str4;
        str3="halters";
        str4="halters";
        System.out.println(str3==str4);
        System.out.println(str3.equals(str4));*/
    }
}

class Ref{
    Ref x;
    public void setRef(Ref r){ x = r;}
    public Ref getRef(){ return x;}
    public String toString(){ 
        String heredado = super.toString(); String mio = "nulo"; 
        if (x != null) mio = x.toString(); 
        return heredado + "\tREF: " + mio;}
}
//Clase de apuntadores