//Sebastián Ochoa 19/07/2025

/*Now our goal is to learn the loops - i.e. repeated actions. Let us find the sum of several numbers (more than two). It will be useful to do this in a loop. As shown in the picture above - you can create variable sum and add every value from the list to it. Perhaps "for" loop will suit nicely since the amount of numbers is known beforehand.

If you have troubles, try Sums In Loop first - it is, probably, easier.

Input data has the following format:

first line contains N - amount of values to sum;
second line contains N values themselves.
Answer should contain a single value - the sum of N values.*/

import java.util.*; import java.io.*;

public class N2SumInLoop{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(), sum=0;
        for (int i=0;i<n;i++) sum+=sc.nextInt();
        System.out.println(sum);
    }
}