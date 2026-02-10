//Sebastián Ochoa 10/02/2026

/*This problem introduces popular algorithm of the "linear search", which should be learnt thoroughly as it is often used in programming more complex tasks (sorting etc.)

Very common operation on sequence of values, or arrays is to find its extremal value - maximum or minimum. To achieve this one need to store current maximum (or minimum respectively) in a separate variable, and then run through array, comparing each of its elements to this variable. Whenever next value is greater than this temporary variable, this value should be copied into it (as a new maximum).

At the end of the pass this temporary variable will hold the extremum value.*/

import java.util.*; import java.io.*;

public class N15MaximumofArray{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); String linea = sc.nextLine(); double menor = 10000000, mayor=-10000000; String[] line = linea.split(" "); sc.close();
        for (int i=0; i<299; i++){int j=Integer.valueOf(line[i]); if(j<menor) menor=j; if(j>mayor) mayor=j;}
        System.out.println((int) mayor+" "+ (int) menor);
    }
}