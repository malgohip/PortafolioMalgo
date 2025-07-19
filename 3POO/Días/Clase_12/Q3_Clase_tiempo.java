import java.util.*;
class tiempo{
    private int agno, mes, dia, hora, minuto, segundo;
    private String mezzogiorno;
    public tiempo(int a, int m, int d,int h,int mi,int s, String md){agno=a; mes=m; dia=d; hora=h; minuto=mi; segundo=s; mezzogiorno=md;}
    public tiempo(){this(0,0,0,0,0,0,"AM");}
    public String toString(){String concat = String.format("%04d/%02d/%02d %02d:%02d:%02d %s", agno, mes, dia, hora, minuto, segundo, mezzogiorno); return concat;}
}

public class Q3_Clase_tiempo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int agn=sc.nextInt(), me=sc.nextInt(), di=sc.nextInt(), ho=sc.nextInt(), min=sc.nextInt(), se=sc.nextInt(); String mezz=sc.next(); sc.close();
        tiempo temp = new tiempo(agn,me,di,ho,min,se,mezz); System.out.println(temp);
    }
}