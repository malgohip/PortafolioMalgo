import java.util.Scanner;

public class Clase_15 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Hi, tell me the lenght of your array: "); int a=in.nextInt(); System.out.println();
        System.out.println("Your array woud be: ");
        MiArr m = new MiArr(a); System.out.println(m); 
        System.out.print("\nNow tell me the your favorite number: "); int b=in.nextInt(); System.out.println();
        System.out.println("Your favorite number is at index: "+m.favorito(b)); System.out.println();
        System.out.print("Tell me the index number for the space: "); int c=in.nextInt(); System.out.println();
        System.out.println(m.hacerEspacio(c).toString());
        System.out.println("Your inverted array woud be: \n");
        m.invertir(); System.out.println(m);
        System.out.println("\nYour orderered array woud be: \n");
        m.ordenBurbuja(); System.out.println(m);
        System.out.print("\nNow tell me the your second favorite number: "); int d=in.nextInt(); System.out.println();
        System.out.println(m.busquedaBin(d));
        in.close();
    }
}
