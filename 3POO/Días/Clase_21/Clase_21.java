import java.util.*;

public class Clase_21{

    public static void main(String[]args){
        ArrayList<Pais> paises = new ArrayList<Pais>();
        paises.add(new Pais("Colombia")); paises.add(new Pais("Brazil")); paises.add(new Pais("Italia")); paises.add(new Pais("Bielorrusia")); paises.add(new Pais("Japon")); paises.add(new Pais("China")); paises.add(new Pais("Australia"));paises.add(new Pais("Nueva Zelanda")); paises.add(new Pais("Sudán")); paises.add(new Pais("Kenia")); paises.add(new Pais("Antartida"));
        paises.set(4,new Pais("Japón"));
        for (Pais p: paises) System.out.println(p);
    }
}

class Pais{
    String pais;
    public Pais(String p){pais=p;}
    public String toString(){return pais;}
}