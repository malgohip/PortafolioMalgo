class Arithmetic{
    void add(int int_1, int int_2){System.out.print(int_1+int_2+" ");}
}

class Adder extends Arithmetic {
    void getSupClass() {System.out.print("Arithmetic\n");}
}

public class N15_Java_Inheritance_II {
    public static void main(String[] args){
        Adder adder = new Adder(); System.out.print("My superclass is: "); adder.getSupClass(); adder.add(19,23); adder.add(7,6); adder.add(15,5);}
}