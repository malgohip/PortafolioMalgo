//Sebastián Ochoa 19/07/2025

/*Most programs should be able to make some choices and decisions. And we are going to practice conditional programming now.
This is usually done by a kind of if ... else statements which may look like:

IF some_condition THEN
    do_something
ELSE
    do_other_thing
ENDIF
Depending on your programming language syntax could be different and else part is almost always optional. You can read more in wikipedia article on Conditional statements.

Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.

Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.
For Answer please enter the same amount of minimums separated by space, for example:*/

import java.util.*; import java.io.*;

public class N4MinimumOfTwo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a = sc.nextInt(), b = sc.nextInt(); if(a<=b) System.out.print(a+" "); else System.out.print(b+" ");}
    }
}