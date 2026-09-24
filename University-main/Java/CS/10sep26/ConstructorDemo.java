class Bookdef 
{
    String title;
    int cost;
}
class Book 
{
   String title;
   int cost;
    Book() {        title = "Untitled Book";        cost = 100;    }
    Book(String t, int c) {        title = t;        cost = c;    }
    int Book(){return 0;} // [WARN] is only raise warning only and it can run successfully. but is  warning ::: this method has a constructor name
    void show() {        System.out.println("Title: " + title + " | Cost: " + cost);    }
}

public class ConstructorDemo {
    public static void main(String[] args) {
        Bookdef def = new Bookdef();
        System.out.println("Bookdef -> Title : " + def.title + " | Cost: " + def.cost);
        
	Book defaultBook = new Book();
        defaultBook.show();

        Book customBook = new Book("Java Basics", 250);
        customBook.show();
    }
}