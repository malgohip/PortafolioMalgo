import java.io.*;

class Result {
    public static String findDay(int month, int day, int year) {
        int anosADias = 0, mesesADias = 0, diasPasados=day-1;
        for (int i = 2000; i < year; i++) {if (esBisiesto(i)) anosADias += 366; else anosADias += 365;}
        for (int i = 1; i < month; i++) {if (i == 2){ if (esBisiesto(year)) mesesADias+=29; else mesesADias+=28;} else if ((i%2)==0){if(i>=8) mesesADias+=31; else mesesADias+=30;} else {if(i<8) mesesADias+=31; else mesesADias+=30;}}
        int diasTotales = anosADias + mesesADias + diasPasados;
        return diaSemana(diasTotales);}

    public static boolean esBisiesto(int year) {return ((year % 4) == 0 && (year % 100) != 0) || ((year % 400) == 0);}

    public static String diaSemana(int diasPasados) {if ((diasPasados%7)==1) return "SUNDAY"; else if ((diasPasados%7)==2) return "MONDAY"; else if ((diasPasados%7)==3) return "TUESDAY"; else if ((diasPasados%7)==4) return "WEDNESDAY"; else if ((diasPasados%7)==5) return "THURSDAY"; else if ((diasPasados%7)==6) return "FRIDAY"; else return "SATURDAY";}
}

public class N12_Java_Date_and_Time {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String outputPath = System.getenv("OUTPUT_PATH"); if (outputPath == null) outputPath = "output.txt";
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(outputPath));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}