import java.util.*;

public class Clase_2{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in); System.out.print("Tell me the voltage: "); int voltage = sc.nextInt();
    if (!(voltage<11 || voltage>14.5)) System.out.println("The voltage is correct :D");
    sc.close();
    System.out.println("END OF PROGRAM.");
  }
}