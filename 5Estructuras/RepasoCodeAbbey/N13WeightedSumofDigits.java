//Sebastián Ochoa 03/09/2025

/*This program resembles more complex algorithms for calculation CRC and other checksums and also hash-functions on character strings. Besides it will provide you with one more exercise on splitting values to decimal digits. You may want to try Sum of Digits before this one.

Let us calculate sum of digits, as earlier, but multiplying each digit by its position (counting from the left, starting from 1). For example, given the value 1776 we calculate such weighted sum of digits (let us call it "wsd") as:

wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60*/

import java.util.*; import java.io.*;

public class N13WeightedSumofDigits{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a=sc.nextInt(); System.out.print(sumaDigitos(a)+" ");}
        sc.close();    
    }

    static int sumaDigitos(int n){String Sn=""+n; int a=0; for (int i=0; i<Sn.length();i++){char c=Sn.charAt(i); a+=(Integer.valueOf(""+c)*(i+1));} return a;}
}