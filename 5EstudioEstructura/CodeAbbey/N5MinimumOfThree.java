//Sebastián Ochoa 19/07/2025

/*To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.*/

import java.util.*; import java.io.*;

public class N5MinimumOfThree{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(); if(a<b){if(a<c) System.out.print(a+" "); else System.out.print(c+" ");} else {if(b<c) System.out.print(b+" "); else System.out.print(c+" ");}}
    }
}
