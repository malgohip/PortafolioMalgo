//Sebastián Ochoa 25/08/2025

/*When we speak about arithmetic progression (or arithmetic sequence) we mean a series of numbers with a special property - each value is followed by the other, greater by predefined amount (step).

I.e. difference of (K+1)-th and K-th values is a constant. Here are examples of sequences

1 2 3 4 5 6 7 ...
4 6 8 10 12 14 16...
10 13 16 19 22 25 28...
Since so, arithmetic sequence is completely defined by the first member (A) and the increment value - step size - (B). First few members could be expressed as

A + (A + B) + (A + 2B) + (A + 3B) + ...
You are to calculate the sum of first members of arithmetic sequence. Wikipedia page on arithmetic progression could be of significant help to one who meets them for the first time.*/

import java.util.*; import java.io.*;

public class N8ArithmeticProgression{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt(), d=0; for (int j=0; j<c; j++) d+=a+j*b; System.out.print(d+" ");}
    }
}