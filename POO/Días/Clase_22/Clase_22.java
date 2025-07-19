import java.util.*;
import java.io.*;

public class Clase_22 {
    public static void main(String[] args)throws IOException {
        Scanner arc =new Scanner(new File("texto.txt"));
        HashMap<String, Integer> dic = new HashMap<String, Integer>();
        while (arc.hasNext()){String j=arc.next(); if (dic.containsKey(j)) dic.replace(j, dic.get(j)+1); else dic.put(j,1);/*dic.put(j,dic.getOrDefault(j, 0)+1);*/}
        System.out.println(dic);
        arc.close();
    }
}