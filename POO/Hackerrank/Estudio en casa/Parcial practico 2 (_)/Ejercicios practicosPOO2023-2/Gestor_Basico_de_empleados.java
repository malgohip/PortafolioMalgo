import java.util.*;

class Empleado{
    String nombre, genero, departamento; int edad, semanasCotizadas; double salario; 
    public Empleado(String nom, int eda, String gen, String dep, int semCot, double sal){nombre=nom; edad=eda; genero=gen; departamento=dep; semanasCotizadas=semCot; salario=sal;}
    public double obtenerBonificacion(){if (semanasCotizadas<=325) return 0.10; else if (semanasCotizadas<=650) return 0.15; else if (semanasCotizadas<=975) return 0.20; else return 0.25;}
    public void AumentarSalario(){salario+=(salario*obtenerBonificacion());System.out.print(salario);}
    public void AumentarSemanasCotizadas(){semanasCotizadas++;}
    public void DerechoPensionarse(){if (semanasCotizadas<1300 || ((genero.equals("H") && edad<62)||(genero.equals("M") && edad<57))) System.out.println("Aun no tiene derecho a la pension"); else System.out.println(nombre+" tiene derecho a la pension"); if (semanasCotizadas<1300) System.out.println("Le hacen falta: "+CuantasSemanasFaltanParaPensioanrse()+" semanas"); else System.out.println("Ya cumplio las semanas");}
    public int CuantasSemanasFaltanParaPensioanrse(){return 1300-semanasCotizadas;}
}

public class Gestor_Basico_de_empleados {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nome=sc.nextLine(); int edad=sc.nextInt(); String gene=sc.next(); sc.nextLine(); String depa=sc.nextLine(); int semaCoti=sc.nextInt(); double sala=sc.nextDouble();
        Empleado guy = new Empleado(nome,edad,gene,depa,semaCoti,sala);
        System.out.print("Su nuevo salario es:"); guy.AumentarSalario(); System.out.println(); guy.DerechoPensionarse(); guy.AumentarSemanasCotizadas();
        System.out.println("Nombre:"+guy.nombre+" edad:"+guy.edad+" genero:"+guy.genero+" departamento:"+guy.departamento+" semanas Cotizadas:"+guy.semanasCotizadas+" Salario:"+guy.salario+" pesos");
        sc.close();
    }
}