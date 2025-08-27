//Sebastián Ochoa 25/08/2025

/*Triangle is an object built of three line segments (sides of triangle), connected by ends. Wiki on triangles provides more detailed explanation.
If we have three line segments with lengths A B C - we either can built a triangle with them
(for example with 3 4 5 or 3 4 7 - though this is with zero area) or we found it impossible
(for example 1 2 4).

You are given several triplets of values representing lengths of the sides of triangles. You should tell from which triplets it is possible to build triangle and for which it is not.*/

import java.util.*; import java.io.*;

public class N9Triangles{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt(), r=1; if (a+b<c) r=0; else if (a+c<b) r=0; else if (b+c<a) r=0; System.out.print(r+" ");} 
    }
}