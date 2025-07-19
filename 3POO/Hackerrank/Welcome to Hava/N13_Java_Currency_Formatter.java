import java.util.*;
import java.text.NumberFormat;
import java.util.Locale;

public class N13_Java_Currency_Formatter {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double amount = sc.nextDouble();
        sc.close();

        String us = USFormat(amount);
        String india = indiaFormat(amount);
        String china = chinaFormat(amount);
        String france = franceFormat(amount);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }

    static String USFormat(double payment){NumberFormat nF = NumberFormat.getCurrencyInstance(Locale.US); return nF.format(payment);}
    static String indiaFormat(double payment){String formatIndia = String.format("Rs.%,3.2f", payment);return formatIndia;}
    static String chinaFormat(double payment){NumberFormat nF = NumberFormat.getCurrencyInstance(Locale.CHINA); return nF.format(payment);}
    static String franceFormat(double payment){NumberFormat nF = NumberFormat.getCurrencyInstance(Locale.FRANCE); return nF.format(payment);}
}