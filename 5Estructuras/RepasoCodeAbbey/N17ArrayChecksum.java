//Sebastián Ochoa 01/09/2026

/*Checksums are small values calculated from big amount of data to test whether data are consistent, i.e. whether they contain errors.

For example if Anna sends some file to Bob, she can calculate its checksum and tell it Bob, who will calculate checksum on the file he received, and compare it with the value told by Anna.

Another, even more common example - any bank card you use has a checksum in the last digit of its number so any device could prevent you from entering wrong number by mistake (you may read more in the exercise on Luhn Algorithm).

For programming several further tasks we'll use similar way to check whether resulting array is correct or not. To avoid problems with such tasks let us now practice the checksum calculating algorithm which will be involved.

You will be given the array for which checksum should be calculated. Perform calculation as follows: for each element of the array (starting from beginning) add this element to result variable and multiply this sum by 113 - this new value taken by modulo 10000007 should become the next value of result, and so on.

Read the article on checksum for detailed description of this algorithm. An example of calculation also could be found there.*/

import java.util.*; import java.io.*;

public class N17ArrayChecksum{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(), res=0; sc.nextLine();
        String[] l = sc.nextLine().split(" "); 
        for (int i=0; i<n; i++){
            res+=(Integer.valueOf(l[i])*113);
            res%=10000007;
        }
        System.out.println(res);
        sc.close();
    }
}