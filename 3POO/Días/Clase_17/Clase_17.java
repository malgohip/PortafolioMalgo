public class Clase_17 {
    public static void main(String[] args) {
        //cuentaRegresiva(3);
        //cRegresiva("ª");
        //System.out.println(pow(3,4));
    }

    static void cuentaRegresiva (int n){
        if (n==0) return;
        cuentaRegresiva(n-1);
        System.out.println(n);
    }

    static String cRegresiva (String n){
        if ("aaa".equals(n)) return "";
        System.out.println(cRegresiva(n+"a"));
        return n;
    }

    static int pow (int base, int expo){
        if (expo==0) return 1;
        return pow(base,expo-1)*base;
    }
}