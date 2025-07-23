//Sebastián Ochoa 23/07/2025

/*When program deals with numbers which have fraction part we sometimes want to round such values to whole integer. We'll need this for programming some later problems (to make answers simpler, for example), so let us have the following dedicated exercise to learn this trick.

There are several pairs of numbers. For each pair you are to divide first by second and return the result, rounded to the nearest integer.

In cases, when result contains exactly 0.5 as a fraction part, value should be rounded "away from zero" (i.e. by adding another 0.5 to positive or substracting from negative value). For more thorough explanations, please refer Wikipedia's article on Rounding - half away from zero.

In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed (unless other is explicitly specified).*/

import java.util.*; import java.io.*;

public class N6Rounding{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){float a = sc.nextFloat(), b = sc.nextFloat(), c = a/b; if(c>=0) {if (c%10>=5) System.out.print((int)c+1+" "); else System.out.print((int)c+" ");} else {if (c%10>=5) System.out.print((int)c+" "); else System.out.print((int)c-1+" ");}}
    }
}