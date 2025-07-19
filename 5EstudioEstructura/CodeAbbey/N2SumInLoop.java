//Sebastián Ochoa 19/07/2025

/*Since starting could be hard sometimes, let us try the simplest problem possible. The goal is to have practice on submitting answers etc.

We need to sum two numbers and tell the result. Though you can do it manually, try to write a simple program in any language you know, or like, or want to learn.*/

import java.util.*; import java.io.*;

public class N2SumInLoop{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(), sum=0;
        for (int i=0;i<n;i++) sum+=sc.nextInt();
        System.out.println(sum);
    }
}