//Sebastián Ochoa 29/08/2025

/*Very common problem in computational programming is to determine the underlying law to which some phenomenon obeys. For learning purpose let us practice a simple variant - discovering linear dependence by two given observations (for example, how the price for some product depends on its size, weight etc.)

Linear function is defined by an equation:

y(x) = ax + b
Where a and b are some constants.
For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
for x = 0, 1, 2, 3...

Your task is to determine a and b by two points, belonging to the function.
I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function equation - and you should restore the equation itself.*/

import java.util.*; import java.io.*;

public class N10LinearFunction{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); int n = sc.nextInt();
        for (int i=0;i<n;i++){int x1=sc.nextInt(), y1=sc.nextInt(), x2=sc.nextInt(), y2=sc.nextInt(), m=(y2-y1)/(x2-x1), c=y1-m*x1; System.out.print("("+m+" "+c+") ");}
    }
}