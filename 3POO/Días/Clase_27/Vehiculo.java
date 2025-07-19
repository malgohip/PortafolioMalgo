public class Vehiculo {
	String placa;
	String dueno;
    
    public Vehiculo(){
		placa = "";
		dueno = "";
	}

	public Vehiculo(String p, String d){
		placa = p;
		dueno = d;
	}
    
	public void avanzar() {
		System.out.println("Este vehiculo avanza: 1");
	}
}