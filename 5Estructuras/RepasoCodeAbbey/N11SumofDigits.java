//Sebastián Ochoa 01/09/2025

/*This programming exercise is intended to introduce numeral system basics to you. We start learninig this concept by playing with decimal system which we use everyday (though you should keep in mind that computer does not use it internally - it only converts numbers to it when they should be shown to user).

As any number greater than 9 is represented by several digits, we can calculate the sum of these digits. For example, for numbers 1492 and 1776 we get:

1 + 4 + 9 + 2 = 16
1 + 7 + 7 + 6 = 21
In this task you will be given several numbers and asked to calculate their sums of digits.

Important: while many programming languages have built-in functions to convert numbers to strings (from which digits could be extracted), you should not use this (since your goal is to learn some programming tricks).

Instead you need to implement algorithm with repetitive division by 10 (base of numeral system) and summing up the remainders. Read the Number to digits article for details on the algorithm.*/

import java.util.*; import java.io.*;

public class N11SumofDigits{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a=sc.nextInt(), b=sc.nextInt(), m=a*b; m+=sc.nextInt(); System.out.print(sumaDigitos(m)+" ");}
        }

    static int sumaDigitos(int n){String Sn=""+n; int a=0; for (int i=0; i<Sn.length();i++){char c=Sn.charAt(i); a+=Integer.valueOf(""+c);} return a;}
}