import java.util.*;

interface Cliente {
    double calcularRiesgo();
    double capacidadDePago();
    String apto(double riesgo, double capacidad);
}

class PersonaNatural implements Cliente{
    private double ingresos; private double deudas;
    public PersonaNatural(double income, double loans){ingresos=income; deudas=loans;}
    public double calcularRiesgo(){return deudas/ingresos;}
    public double capacidadDePago(){return ingresos-deudas;}
    public String apto(double riesgo, double capacidad){if (riesgo<0.5&&capacidad>1000) return "Apto"; else return "No Apto";}
}

class EmpresaPequegna implements Cliente{
    private double ingresos; private double deudas; private int numeroEmpleados;
    public EmpresaPequegna(double income, double loans, int staff){ingresos=income; deudas=loans; numeroEmpleados=staff;}
    public double calcularRiesgo(){return (deudas/ingresos)*(1.0/numeroEmpleados);}
    public double capacidadDePago(){return ingresos-deudas-(numeroEmpleados*500);}
    public String apto(double riesgo, double capacidad){if (riesgo<0.4&&capacidad>5000) return "Apto"; else return "No Apto";}
}

class GranCorporacion implements Cliente{
    private double ingresos; private double deudas; private double patrimonio; private int numeroEmpleados;
    public GranCorporacion(double income, double loans,double patrimony, int staff){ingresos=income; deudas=loans; patrimonio=patrimony; numeroEmpleados=staff;}
    public double calcularRiesgo(){return (deudas/(ingresos+patrimonio))*(1.0/Math.log(numeroEmpleados+1));}
    public double capacidadDePago(){return (ingresos+patrimonio)-deudas-(numeroEmpleados*1000);}
    public String apto(double riesgo, double capacidad){if (riesgo<0.3&&capacidad>20000) return "Apto"; else return "No Apto";}
}

public class SistemaBancarioPolimorfismo{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(); sc.nextLine(); 
        for (int i=0; i<n; i++){
            String[] cliente = sc.nextLine().split(" "); 
            if (cliente[0].equals("PersonaNatural")){
                Cliente client = new PersonaNatural(Double.valueOf(cliente[1]), Double.valueOf(cliente[2])); 
                System.out.println("Persona Natural: Riesgo: "+client.calcularRiesgo()+", Capacidad de Pago: "+client.capacidadDePago()+", Resultado: "+client.apto(client.calcularRiesgo(), client.capacidadDePago()));
            }
            else if (cliente[0].equals("EmpresaPequena")){
                Cliente client = new EmpresaPequegna(Double.valueOf(cliente[1]), Double.valueOf(cliente[2]), Integer.valueOf(cliente[3])); 
                System.out.println("Empresa Pequena: Riesgo: "+client.calcularRiesgo()+", Capacidad de Pago: "+client.capacidadDePago()+", Resultado: "+client.apto(client.calcularRiesgo(), client.capacidadDePago()));
            }
            else if (cliente[0].equals("GranCorporacion")){
                Cliente client = new GranCorporacion(Double.valueOf(cliente[1]), Double.valueOf(cliente[2]), Double.valueOf(cliente[3]), Integer.valueOf(cliente[4]));
                System.out.println("Gran Corporacion: Riesgo: "+client.calcularRiesgo()+", Capacidad de Pago: "+client.capacidadDePago()+", Resultado: "+client.apto(client.calcularRiesgo(), client.capacidadDePago()));
            }
        }
        sc.close();
    }
}