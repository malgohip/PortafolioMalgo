import java.util.*;

public class N9_Java_End_of_file {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int j =0;
        while (sc.hasNextLine()){ 
            String linea=sc.nextLine(); j++;
            if (linea == null) break;
            System.out.println(j + " " +linea);  
            if (linea.endsWith("end-of-file.")) break;
            }
        sc.close();
    }
}

//FUERON 2 PUTAS SEMANAS