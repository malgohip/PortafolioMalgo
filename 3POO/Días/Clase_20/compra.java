public class compra{
    private String nombre; private int precio, cantidad; private time hora;
    public compra(String nom, int pre, int cant, time hor){nombre=nom; precio= pre; cantidad=cant; hora=hor;}
    public String toString(){return "Nombre: "+nombre+"\nPrecio: "+precio+"\nCantidad: "+cantidad+"\nTotal: "+(precio*cantidad)+"\nFecha: "+hora;}
}