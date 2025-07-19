//Sebastián Ochoa 19/07/2025

/*If you already learned how to write program with a simple loop from Sum in Loop task, this new exercise will be just a simple modification.

Now we are given several pairs of values and we want to calculate sum for each pair.

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.*/

import java.util.*; import java.io.*;

public class N3SumsInLoop{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a = sc.nextInt(), b = sc.nextInt(); System.out.print(a+b+" ");}
    }
}