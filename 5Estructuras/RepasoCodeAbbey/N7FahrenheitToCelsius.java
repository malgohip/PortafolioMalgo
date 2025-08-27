//Sebastián Ochoa 25/08/2025

/*There are two widespread systems of measuring temperature - Celsius and Fahrenheit. First is quite popular in Europe and second is well in use in United States for example.

By Celsius scale water freezes at 0 degrees and boils at 100 degrees. By Fahrenheit water freezes at 32 degrees and boils at 212 degrees. You may learn more from wikipedia on Fahrenheit. Use these two points for conversion of other temperatures.

You are to write program to convert degrees of Fahrenheit to Celsius.*/

import java.util.*; import java.io.*;

public class N7FahrenheitToCelsius{

    static int rounder(float c){
        if(c>=0){if ((c%1)*10>=5) return((int)c+1); else return((int)c);} else {if ((c%1)*10>=5) return((int)c); else return((int)c-1);}
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int f = sc.nextInt(); float c = (f-32)*(float) 5/9; System.out.print(rounder(c)+" ");}
    }
}