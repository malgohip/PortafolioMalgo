//Sebastián Ochoa 03/09/2025

/*This task provides practice for core property of remainder taking operation in arithmetic - persisting of the remainder over addition and multiplication. This important property is often used for checking results of calculations, in competitive programming, in calculation checksums and especially for encryption.
See Modular arithmetic for thorough explanations.

We have a kind of long arithmetic calculation here, and we are asked about the result modulo some number (result % M in many languages).*/

import java.util.*; import java.io.*;

public class N14ModularCalculator{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); double n = (double) sc.nextInt(); sc.nextLine(); double r=0;
        while (sc.hasNext()) {
            String s = sc.nextLine(); String[] lin = s.split(" ");
            if (lin[0].equals("+")) n+=(Integer.valueOf(lin[1]));
            else if (lin[0].equals("*")) n*=(Integer.valueOf(lin[1]));
            else r = n%(Integer.valueOf(lin[1]));
            System.out.print("Prueba: "+n+" ");
        }
        System.out.println((int) r);
        sc.close();
    }
}