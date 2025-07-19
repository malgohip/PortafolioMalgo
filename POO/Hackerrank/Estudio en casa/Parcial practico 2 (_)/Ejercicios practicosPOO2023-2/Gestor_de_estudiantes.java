import java.util.*;

class Alumno{
    String nombre; int edad; ArrayList<Double> notas;
    public Alumno(String no, int ed, ArrayList<Double> nota){nombre=no; edad=ed; notas=nota;}
    public void agregarNota(double nota){notas.add(nota);}
    public double calcularPromedio(){double sumatoria=0; for (int i=0; i<notas.size(); i++){sumatoria+=(double)notas.get(i);} double promedio = sumatoria/notas.size(); return promedio;}
    public double obtenerMejorNota(){double mayor=0; for (int i=0; i<notas.size(); i++) if ((double)notas.get(i)>mayor) mayor=(double)notas.get(i); return mayor;}
    public double obtenerPeorNota(){double menor=5.1; for (int i=0; i<notas.size(); i++) if ((double)notas.get(i)<menor) menor=(double)notas.get(i); return menor;}
    public void mostrarInformacion(){System.out.println("Nombre: "+nombre+"\nEdad: "+edad+"\nPromedio de Notas: "+calcularPromedio()+"\nMejor Nota: "+obtenerMejorNota()+"\nPeor Nota: "+obtenerPeorNota());}
}

public class Gestor_de_estudiantes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nom=sc.nextLine(); int eda = sc.nextInt(); ArrayList<Double> nots = new ArrayList<Double>();
        Alumno Arnulfo = new Alumno(nom,eda,nots); double not = sc.nextDouble(); 
        while (not!=-1){Arnulfo.agregarNota(not); not = sc.nextDouble();}
        sc.close();
        Arnulfo.mostrarInformacion();
    }
}