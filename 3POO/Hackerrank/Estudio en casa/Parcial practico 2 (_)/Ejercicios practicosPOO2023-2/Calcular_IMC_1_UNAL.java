import java.util.*;

class Persona{
    String nombre; int edad; char genero; double peso, altura;
    Persona(){nombre="Pepito"; edad=69; genero='N'; peso=42.0; altura=1.69;}
    Persona(String no, int ed,char  ge, double pe, double al){nombre=no; edad=ed; genero=ge; peso=pe; altura=al;}
    public double calcularIMC(){double IMC = peso/(altura*altura);return IMC;}
    public Boolean esMayorDeEdad(){if (edad >= 18) return true; else return false;}
    public String toString(){String concat =""; concat+=calcularIMC()+"\n"; concat+="Mayor de edad: "+esMayorDeEdad()+"\n"; concat+="Nombre:"+nombre+" edad:"+edad+" genero:"+genero+" peso:"+peso+" altura:"+altura; return concat;}
}

public class Calcular_IMC_1_UNAL{
    public static void main(String[] args) {Scanner sc = new Scanner(System.in); String nom = sc.nextLine(); int eda = sc.nextInt(); char gen = sc.next().charAt(0); double pes = sc.nextDouble(), alt = sc.nextDouble(); System.out.println(new Persona(nom, eda, gen, pes, alt)); sc.close();}
}