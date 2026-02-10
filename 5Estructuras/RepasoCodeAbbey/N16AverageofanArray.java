//Sebastián Ochoa 10/02/2026

/*Important branch of mathematics which heavily uses programming is statistics - i.e. calculation of characteristics for some data. (Just think of statistics of visitors / pageviews of the web-site etc.) Learning this discipline is usually started from acquaintance with an average value.

Average (or mean) value of some numbers could be calculated as their sum divided by their amount. For example:

avg(2, 3, 7) = (2 + 3 + 7) / 3 = 4
avg(20, 10) = (20 + 10) / 2 = 15
You will be given several arrays, for each of which you are to find an average value.*/

import java.util.*; import java.io.*;

public class N16AverageofanArray{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt(); 
        for (int i=0; i<n; i++){
            String[] l = sc.nextLine().split(" "); int sum=0;
            for (int j=0; j<l.length; j++){
                sum+=Integer.valueOf(l[j]);
            }
            int avr=(int) sum/l.length; System.out.print(avr+" ");
            }
        sc.close();
    }
}