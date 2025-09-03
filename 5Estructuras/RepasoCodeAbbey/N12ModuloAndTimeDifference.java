//Sebastián Ochoa 03/09/2025

/*Dealing with remainders may cause heavy headache to novice programmers. Let us write a simple program which has this operation for its core to study integer division better. At the same time we'll have some practice in handing dates - which sometimes gives headache even to experienced coders.

In arithmetic, the remainder (or modulus) is the amount "left over" after performing the division of two integers which do not divide evenly (from Wiki). This task will provide further practice with modulo operation.

Suppose, we are given two timestamps - for example, when the train or ferry boat starts its travel and when it finishes. This may look like:

start: May 3, 17:08:30
end  : May 8, 12:54:15
and we are curious to know, how much time (in days, hours, minutes and seconds) is spent in traveling (perhaps, to choose faster variant). How this could be achieved?

One of the easiest way is:

convert both timestamps to big numbers, representing seconds from the beginning of the month (or year, or century);
calculate their difference - i.e. travel time in seconds;
convert this difference back to days, hours, minutes and seconds.
First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. and summing all values up.
The third operation should be performed on contrary by several divisions with keeping remainders.

In this task we are given several pair of timestamps. We suppose that both dates in the pair are always in the same month, so only number of day will be given. We want to calculate difference between timestamps in each pair.*/

import java.util.*; import java.io.*;

public class N12ModuloAndTimeDifference{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int d1 = sc.nextInt(), h1 = sc.nextInt(), m1 = sc.nextInt(), s1 = sc.nextInt(), d2 = sc.nextInt(), h2 = sc.nextInt(), m2 = sc.nextInt(), s2 = sc.nextInt(), t1 = (((((d1*24)+h1)*60)+m1)*60)+s1, t2 = (((((d2*24)+h2)*60)+m2)*60)+s2, t = t2-t1, d = (int) t/86400, h = (int) (t-(d*86400))/3600, m = (int) (t-(d*86400)-(h*3600))/60, s = t-(d*86400)-(h*3600)-(m*60); System.out.print("("+d+" "+h+" "+m+" "+s+") ");}
        sc.close();    
    }
}