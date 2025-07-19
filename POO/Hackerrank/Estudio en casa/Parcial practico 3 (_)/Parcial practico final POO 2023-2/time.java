public class time{
    private int agno, mes, dia, hora, minuto, segundo; private String mediodia;
    public time(int ag, int me, int di, int ho, int mi, int se, String med){agno=ag; mes=me; dia=di; hora=ho; minuto=mi; segundo=se; mediodia=med;}
    public String agnadirCeros(int momento){if (momento<10) return ""+0+momento; else return ""+momento;}
    public String toString(){return ""+agno+"/"+agnadirCeros(mes)+"/"+agnadirCeros(dia)+" "+agnadirCeros(hora)+":"+agnadirCeros(minuto)+":"+agnadirCeros(segundo)+" "+mediodia;}
}