import java.util.*;

class minutosCambio_II{
    private long anos, dias;
    public minutosCambio_II(long m){anos = m/(1440*365); dias = (m%(1440*365))/1440;}
    public String toString(){String concat =anos+" year(s) and "+dias+" day(s)";return concat;}
}

public class Q5_Clase_Minutos_a_Anos_y_Dias{
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);long min=sc.nextLong(); sc.close();        
        minutosCambio_II minu = new minutosCambio_II(min); System.out.println(minu);
    } 
}