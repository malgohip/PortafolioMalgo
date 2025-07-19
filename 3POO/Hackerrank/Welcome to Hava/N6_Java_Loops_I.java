import java.io.*;

public class N6_Java_Loops_I {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine().trim());
        bufferedReader.close();

        for (int i=1;i<=10;i++){int mul = i*N; System.out.printf("%d x %d = %d\n",N,i,mul);}
    }
}