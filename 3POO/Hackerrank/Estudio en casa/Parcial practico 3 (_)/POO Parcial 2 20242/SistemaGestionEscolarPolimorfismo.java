import java.util.*;

interface curso{
    float calcularNotaFinal(int examen, int tarea, int proyecto);
    String estaAprobado(double notafinal);
    String rendimiento(double notafinal);
}

class CursoRegular implements curso{
    public float calcularNotaFinal(int examen, int tarea, int proyecto){
        return (((float)examen*60+tarea*30+proyecto*10)/100);
    }

    public String estaAprobado(double notafinal){
        if (notafinal >= 60) return "Aprobado"; return "No Aprobado";
    }

    public String rendimiento(double notafinal){
        if (notafinal>=90) return "Excelente";
        else if (notafinal>=75) return "Bueno";
        else if (notafinal>=60) return "Suficiente";
        else return "Insuficiente";
    }
}

class CursoAvanzado implements curso{
    public float calcularNotaFinal(int examen, int tarea, int proyecto){
        return (((float)examen*70+tarea*10+proyecto*20)/100);
    }

    public String estaAprobado(double notafinal){
        if (notafinal >= 70) return "Aprobado"; return "No Aprobado";
    }

    public String rendimiento(double notafinal){
        if (notafinal>=90) return "Excelente";
        else if (notafinal>=80) return "Bueno";
        else if (notafinal>=70) return "Suficiente";
        else return "Insuficiente";
    }

}

class Taller implements curso{
    public float calcularNotaFinal(int examen, int tarea, int proyecto){
        return (((float)examen*30+tarea*20+proyecto*50)/100);
    }

    public String estaAprobado(double notafinal){
        if (notafinal >= 65) return "Aprobado"; return "No Aprobado";
    }

    public String rendimiento(double notafinal){
        if (notafinal>=85) return "Excelente";
        else if (notafinal>=75) return "Bueno";
        else if (notafinal>=65) return "Suficiente";
        else return "Insuficiente";
    }

}

public class SistemaGestionEscolarPolimorfismo {
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in); int cant = sc.nextInt(); sc.nextLine(); String concat="";
        for (int i=0; i<cant; i++){
            String cur = sc.nextLine(); cur+="\n"; ArrayList<String> palabras=separaPalabras(cur);
            String respuesta = toStringRetorno(palabras,i); concat+=respuesta;
        }
        System.out.println(concat.substring(0,concat.length()-2)); sc.close();
    }

    static ArrayList<String> separaPalabras(String linea) {
        ArrayList<String> palabras = new ArrayList<String>(); String palabra = "";
        for (int i=0; i<linea.length()-1; i++){
            char letra = linea.charAt(i); if(!(Character.isWhitespace(letra))) palabra+=letra; if (Character.isWhitespace(linea.charAt(i+1)) && !(palabra.equals(""))){palabras.add(palabra); palabra="";}}
        return palabras;
    }

    static String toStringRetorno(ArrayList<String> palabras, int i){
       if (palabras.get(0).equals("CursoRegular")) {CursoRegular jur = new CursoRegular(); 
                float notaFinal=jur.calcularNotaFinal(Integer.valueOf(palabras.get(1)), Integer.valueOf(palabras.get(2)), Integer.valueOf(palabras.get(3)));
                String aprobo=jur.estaAprobado(notaFinal), rindio=jur.rendimiento(notaFinal);
                return "Curso "+(i+1)+" ("+palabras.get(0)+"):\n"+"Nota Final: "+notaFinal+"\n" +"Estado: "+aprobo+"\n"+"Rendimiento: "+rindio+"\n\n";
            }
            else if (palabras.get(0).equals("CursoAvanzado")) {CursoAvanzado jur = new CursoAvanzado(); 
                float notaFinal=jur.calcularNotaFinal(Integer.valueOf(palabras.get(1)), Integer.valueOf(palabras.get(2)), Integer.valueOf(palabras.get(3)));
                String aprobo=jur.estaAprobado(notaFinal), rindio=jur.rendimiento(notaFinal);
                return "Curso "+(i+1)+" ("+palabras.get(0)+"):\n"+"Nota Final: "+notaFinal+"\n" +"Estado: "+aprobo+"\n"+"Rendimiento: "+rindio+"\n\n";
            } 
            else {Taller jur = new Taller(); 
                float notaFinal=jur.calcularNotaFinal(Integer.valueOf(palabras.get(1)), Integer.valueOf(palabras.get(2)), Integer.valueOf(palabras.get(3)));
                String aprobo=jur.estaAprobado(notaFinal), rindio=jur.rendimiento(notaFinal);
                return "Curso "+(i+1)+" ("+palabras.get(0)+"):\n"+"Nota Final: "+notaFinal+"\n" +"Estado: "+aprobo+"\n"+"Rendimiento: "+rindio+"\n\n";
            }
    }
}