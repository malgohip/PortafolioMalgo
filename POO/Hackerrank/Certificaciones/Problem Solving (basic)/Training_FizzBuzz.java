import java.io.*;

class Result {
    public static void fizzBuzz(int n) {for (int i=0; i<(n+1);i++){if ((i%3==0) && (i%5==0)) System.out.println("FizzBuzz"); else if (i%3==0) System.out.println("Fizz"); else if (i%5==0) System.out.println("Buzz"); else System.out.println(i);}}
}

public class Training_FizzBuzz {
    public static void main(String[] args) throws IOException {BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in)); int n = Integer.parseInt(bufferedReader.readLine().trim()); Result.fizzBuzz(n); bufferedReader.close();}
}
