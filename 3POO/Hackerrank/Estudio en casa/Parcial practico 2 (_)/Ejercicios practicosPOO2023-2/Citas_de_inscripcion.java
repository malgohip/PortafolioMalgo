import java.util.*;
import java.io.*;

class Estudiante{
    String nombre, documento; int discapacidad, PEAMA, dobleTitulacion, traslado, reingreso, avance, encuestaDocente; float PAPI;
    public Estudiante(String nom, String doc, int dis, int PEA, int doblTitu, int tra, int rei, int ava, int encDoce, float PAP){nombre=nom; documento=doc; discapacidad=dis; PEAMA=PEA; dobleTitulacion=doblTitu; traslado=tra; reingreso=rei; avance=ava; encuestaDocente=encDoce; PAPI=PAP;}
    public double obtenerPonderadoPrioridad(){return (discapacidad*45+PEAMA*10+dobleTitulacion*6+traslado*6+reingreso*6+avance*4+encuestaDocente*2+(PAPI/5)*1)/80;}
}

class time{
    int dia=22, mes=3, agno=2023, hora=7, minuto=0, segundo=0;
    public time (int orden){if (orden>0){minuto+=orden*45; if (minuto>=60){hora += ((int)minuto/60); minuto = (minuto%60);} if (hora>=16){dia+=((int)(hora-7)/9); hora=((hora-7)%9)+7;}}}
    public String toStringFecha(){return ""+dia+"/"+mes+"/"+agno;}
    public String toStringHora(){String concat = String.format("%02d:%02d:%02d", hora, minuto, segundo); return concat;}
}

public class Citas_de_inscripcion {
    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(new File("citasTestCase3.txt"));
        int cant=sc.nextInt(); sc.nextLine(); sc.nextLine();
        ArrayList<Estudiante> Estudiantes = new ArrayList<Estudiante>();
        ArrayList<Double> Ponderados = new ArrayList<Double>();
        for (int i=0;i<cant;i++){
            String nome=sc.nextLine();
            if ((nome.substring(0,10)).equals("Estudiante")) {
                nome=nome.substring(12,nome.length()-1); 
                String docu=sc.nextLine(); docu=docu.substring(11,docu.length()-1); 
                String disca=sc.nextLine(); int discabo=checkInfo(disca,41);
                String PEA=sc.nextLine(); int PEAbo=checkInfo(PEA,63);
                String dobTit=sc.nextLine(); 
                String dobTitr=dobTit.substring(33,35); 
                int dobTitbo=0; if (dobTitr.equals("Si")){String fedobTit = dobTit.substring(67,dobTit.length()-1); if (fedobTit.substring(fedobTit.length()-4,fedobTit.length()).equals("2023")){int mes=Integer.valueOf(fedobTit.substring(3,4)); if(1<=mes && mes<=7) dobTitbo=1;}} 
                String tras=sc.nextLine(); int trasbo=checkInfo(tras,69);
                String rein=sc.nextLine(); int reinbo=checkInfo(rein,25);
                String avan=sc.nextLine(); avan=avan.substring(19,avan.length()-2); int avanbo=0; int avanint=Integer.valueOf(avan); if (avanint>=70) avanbo=1;
                String enDoc=sc.nextLine(); int enDocbo=checkInfo(enDoc,32);
                String PAPI=sc.nextLine(); PAPI=PAPI.substring(7,PAPI.length()); float PAPIflo=Float.valueOf(PAPI);
                if (sc.hasNextLine()) sc.nextLine();
                Estudiante Federico = new Estudiante(nome,docu,discabo,PEAbo,dobTitbo,trasbo,reinbo,avanbo,enDocbo,PAPIflo);
                Estudiantes.add(Federico);
                Ponderados.add(Federico.obtenerPonderadoPrioridad());
            }
            else{
                while(!(sc.nextLine().equals("")));
            }
        }
        sc.close();
        Estudiantes=bubbleSortPonderados(Estudiantes, Ponderados);
        for (int k=0; k<Estudiantes.size(); k++) {time fechaCita=new time(k); System.out.println("Cita para "+Estudiantes.get(k).nombre+" cc "+Estudiantes.get(k).documento+" el dia "+fechaCita.toStringFecha()+" a las "+fechaCita.toStringHora()+" horas");}
    }

    public static int checkInfo(String info, int ini){
        info=info.substring(ini,info.length()-1);
        int infob=0; if (info.equals("Si")) infob = 1; 
        return infob;
    }

    public static ArrayList<Estudiante> bubbleSortPonderados(ArrayList<Estudiante> Estudiantes, ArrayList<Double> Ponderados){
        for (int i=0; i<Estudiantes.size()-1; i++)
            for (int j=0; j<Estudiantes.size()-i-1; j++)
                if (Ponderados.get(j)<Ponderados.get(j+1)){
                    double temp_1=Ponderados.get(j); Ponderados.set(j, Ponderados.get(j+1)); Ponderados.set(j+1, temp_1);
                    Estudiante temp_2=Estudiantes.get(j); Estudiantes.set(j, Estudiantes.get(j+1)); Estudiantes.set(j+1, temp_2);
                }
        return Estudiantes;
    }
}