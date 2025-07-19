import java.util.*;

public class Clase_10 {
    public static void main(String[] args){

        /*Scanner in = new Scanner(System.in);
        int len;
        System.out.print("How many numbers? ");
        len=in.nextInt();
        int n[] = new int[len];
        //n[0]= 3; n[1]= 23; n[2]= 43; 
        for (int i=0; i<n.length; i++){
            System.out.print("Enter number "+(i+1)+": ");
            n[i]=in.nextInt();
        }
        in.close();
        for (int i=0; i<n.length; i++)
            System.out.print(n[i]+"\t");
            System.out.print("\n");*/
        /*int m[] = {43,23,3,103};
        for (int i=0; i<m.length; i++)
            System.out.print(m[i]+"\t");*/

        /*int len = 5;
        int n[] = new int[len];
        int i;
        System.out.println("Hi, on this array you can enter up to "+len+" numbers or, if you don't wanna enter more numbers, enter a negative and it stops. :D");
        Scanner sc = new Scanner(System.in);
        for (i=0; i<n.length; i++){
            System.out.print("Enter number "+(i+1)+": ");
            int a=sc.nextInt();
            if (a<0) break;
            n[i]=a;
        }
        sc.close();
        System.out.println(n);
        for (int j=0; j<i; j++)
            System.out.print(n[j]+"\t");
        System.out.print("\n");*/

        /*Numero arreglo[] = crearArreglo();
        imprimirArreglo(arreglo);*/

        /*for (int i=0; i<args.length; i++)
            System.out.println("String "+(i+1)+" "+args[i]);*/

        Scanner in = new Scanner(System.in);
        int arreglo[] = crearArreglo(5);
        imprimirArreglo(arreglo);
        System.out.print("Which value do you wanna for len: ");
        int a=in.nextInt();
        System.out.print("\n");
        imprimirArreglo(crearArreglo(a));
        in.close();
    }

    /*public static Numero[] crearArreglo(){
        int len = 5;
        Numero n[] = new Numero[len];
        for (int i=0; i<n.length; i++){
            n[i] = new Numero();
            n[i].set(i+4);
        }
        return n;
    }
    

    public static void imprimirArreglo(Numero[] n){
        System.out.println(n);
        for (int i=0; i<n.length; i++)
            System.out.print(n[i].toString()+"\t");
        System.out.print("\n");
    }*/

    public static int[] crearArreglo(int len){
        int n[] = new int[len];
        for (int i=0; i<n.length; i++){
            n[i] =(i*len);
        }
        return n;
    }

    /*public static int[] crearArreglo(int len){
        int len = 5;
        int n[] = new int[len];
        System.out.println("Hi, on this array you can enter up to "+len+" numbers or, if you don't wanna enter more numbers, enter a negative and it stops. :D");
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<n.length; i++){
            System.out.print("Enter number "+(i+1)+": ");
            int a=sc.nextInt();
            if (a<0) break;
            n[i]=a;
        }
        sc.close();
        return n;
    }*/

    public static void imprimirArreglo(int[] n){
        /*int cont;
        for (int i=0; i<n.length; i++){
            if (n[i] != 0) cont=i;
        }*/

        for (int i=0; i<n.length; i++){
            //if (n[i] == 0 && n[i+1] == 0) break;
            System.out.print(n[i]+"\t");
        }
        System.out.print("\n");
    }
}
