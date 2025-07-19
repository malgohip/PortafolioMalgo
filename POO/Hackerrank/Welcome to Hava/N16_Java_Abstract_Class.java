import java.util.*;

abstract class Book{
    String title;
    abstract void setTitle(String s);
    String getTitle(){return title;}
}

class Novel extends Book {
    void setTitle(String titlexd){title=titlexd;}
}

public class N16_Java_Abstract_Class {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); String title = sc.nextLine(); sc.close();
        Novel novel = new Novel(); novel.setTitle(title); System.out.println("The title is: "+novel.getTitle()); 
    }
}