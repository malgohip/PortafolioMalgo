import java.util.*;

class minutosCambio{
    private long milenios, siglos, decadas, anos, minutos; 
    private float dias;
    public minutosCambio(long m){
        milenios = (m-(m%525960000))/525960000;
        siglos = ((m%525960000)-(m%52596000))/52596000;
        decadas = ((m%52596000)-(m%5259600))/5259600;
        anos = ((m%5259600)-(m%525960))/525960;
        dias = (((float)m%525960)-((float)m%1440))/1440; if ((dias%1)!=0 && (dias%1)<0.5) dias = dias + 1; 
        minutos = m%1440;
    }
    public String toString(){
        String concat=""; 
        if(milenios !=0) {concat+=milenios+" milenio"; if (milenios>1) concat+="s ";else concat+=" ";}
        if(siglos !=0) {concat+=siglos+" siglo"; if (siglos>1) concat+="s "; else concat+=" ";}
        if(decadas !=0) {concat+=decadas+" d\u00e9cada"; if (decadas>1) concat+="s "; else concat+=" ";}
        if(anos !=0) {concat+=anos+" a\u00f1o"; if (anos>1) concat+="s "; else concat+=" ";}
        if(dias !=0) {String concatdias=String.format("%.0f d\u00eda", dias); concat+=concatdias; if (dias>1) concat+="s "; else concat+=" ";}
        if(minutos != 0) {concat+=minutos+" minuto"; if (dias>1) concat+="s";}
        return concat;
    }
}

public class Q1_Minuto_a_Milenios_Siglos_Decadas_Años_y_Dias {
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);long min=sc.nextLong(); sc.close();        
        minutosCambio minu = new minutosCambio(min); System.out.println(minu);
    } 
}