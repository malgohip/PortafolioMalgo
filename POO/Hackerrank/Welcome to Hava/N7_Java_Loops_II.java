import java.util.Scanner;

public class N7_Java_Loops_II {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){ int a = in.nextInt(), b = in.nextInt(), n = in.nextInt(), suma = a;
            for(int k=0;k<n;k++){ suma+=(Math.pow(2,k)*b); System.out.printf("%d ",suma);}
            System.out.print("\n");
        }
        in.close();
    }
}