import java.util.*; import java.io.*;

class persona{
    String nombre; String apellidos; persona[] padres;
    public persona(String name){String[] fullName=name.split(" "); nombre=fullName[0]; apellidos=fullName[1]+" "+fullName[2];}
    public String toString(){return nombre+" "+apellidos;}
}

public class ancestros {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(new File ("ancestros.txt")); int n = sc.nextInt(); sc.nextLine(); persona[] familia = new persona[n];
        for (int i=0; i<n; i++) familia[i]=new persona(sc.nextLine());
        System.out.println(desendencia(sc.nextInt()-1, familia));
        sc.close();
    }

    public static String desendencia(int m, persona[] familia){
        if (m!=0){
            if (m%2==0){return familia[m]+" padre de "+desendencia((m-1)/2, familia);}
            else {return familia[m]+" madre de "+desendencia((m-1)/2, familia);}
        }
        else 
            return ""+familia[m];
    }
}