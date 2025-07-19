import java.util.*; import java.io.*;

class MotoAutomatica extends Vehiculo{
    public MotoAutomatica(String p, String d){placa = p; dueno = d;}
    public void avanzar() {System.out.println("Este vehiculo avanza: 2");}
}

class MotoClasica extends Vehiculo{
    public MotoClasica(String p, String d){placa = p; dueno = d;}
    public void avanzar() {System.out.println("Este vehiculo avanza: 4");}
}

class CarroAutomatico extends Vehiculo{
    public CarroAutomatico(String p, String d){placa = p; dueno = d;}
    public void avanzar() {System.out.println("Este vehiculo avanza: 2");}
}

class CarroManual extends Vehiculo{
    public CarroManual(String p, String d){placa = p; dueno = d;}
    public void avanzar() {System.out.println("Este vehiculo avanza: 4");}
}

public class HerenciayDiccionariosPOO {
    public static void main(String[] args) throws IOException{
        HashMap<String,HashMap<String,ArrayList<Vehiculo>>> Vehiculos = new HashMap<>(); 
        HashMap<String,ArrayList<Vehiculo>> carros = new HashMap<>();
        ArrayList<Vehiculo> Cmanuales =new ArrayList<>(); carros.put("CarroManual",Cmanuales);
        ArrayList<Vehiculo> Cautomaticos =new ArrayList<>(); carros.put("CarroAutomatico",Cautomaticos);
        ArrayList<Vehiculo> Cna =new ArrayList<>(); carros.put("CarroNA",Cna);
        Vehiculos.put("Carro",carros);
        HashMap<String,ArrayList<Vehiculo>> motos = new HashMap<>();
        ArrayList<Vehiculo> Mclasicas =new ArrayList<>(); motos.put("MotoClasica",Mclasicas);
        ArrayList<Vehiculo> Mautomaticas =new ArrayList<>(); motos.put("MotoAutomatica",Mautomaticas);
        ArrayList<Vehiculo> Mna =new ArrayList<>(); motos.put("MotoNA",Mna);
        Vehiculos.put("Moto",motos);
        Scanner sc= new Scanner(new File("HerenciayDiccionariosPOO.txt")); 
        int n = sc.nextInt(); sc.nextLine();
        for (int i=0; i<n; i++){
            String[] vehiculostr = sc.nextLine().trim().split(" "); String tipo=vehiculostr[0]; String[] datos = {}; if(vehiculostr[1].equals("sin")) datos=vehiculostr[2].split(","); else datos=vehiculostr[1].split(",");
            if (tipo.equals("Carro")){
                if (datos[0].equals("manual")){Vehiculo vehiculo = new CarroManual(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Carro").get("CarroManual").add(vehiculo);}
                else if (datos[0].equals("automatico")){Vehiculo vehiculo = new CarroAutomatico(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Carro").get("CarroAutomatico").add(vehiculo);}
                else{Vehiculo vehiculo = new Vehiculo(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Carro").get("CarroNA").add(vehiculo);}
            }
            else if (tipo.equals("Moto")){
                if (datos[0].equals("clasica")){Vehiculo vehiculo = new MotoClasica(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Moto").get("MotoClasica").add(vehiculo);}
                else if (datos[0].equals("automatica")){Vehiculo vehiculo = new MotoAutomatica(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Moto").get("MotoAutomatica").add(vehiculo);}
                else{Vehiculo vehiculo = new Vehiculo(datos[1],datos[2].concat(" "+vehiculostr[vehiculostr.length-1])); Vehiculos.get("Moto").get("MotoNA").add(vehiculo);}
            }
        }
        System.out.println(Vehiculos);
        int m = sc.nextInt(); sc.nextLine();
        for (int j=0; j<m; j++) {
            String placa = sc.nextLine(); 
            for (String a: Vehiculos.keySet()){
                for (String b: Vehiculos.get(a).keySet()){
                    for (Vehiculo veh: Vehiculos.get(a).get(b)){
                        if (placa.equals(veh.placa)){
                            System.out.println("La cantidad de vehiculos /"+b+"/ es: "+Vehiculos.get(a).get(b).size());
                            System.out.println("El tipo de vehiculo es: "+a);
                            System.out.println("El dueno del vehiculo es: "+veh.dueno);
                            veh.avanzar();
                        }
                    }
                }
            }
        }
        sc.close();
    }
}
