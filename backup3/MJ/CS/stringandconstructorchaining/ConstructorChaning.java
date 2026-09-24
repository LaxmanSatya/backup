/*public class ConstructorChaning {
    /// [Q]::: What is the use of this technique?
    class Book {
    String title;
    int cost;
    int yop;

    Book() {        this("Untitled Book", 0);     }

    Book(String t, int c) {        this(t, c, 0);     }

    Book(String t, int c, int y) {        title = t;        cost = c;        yop = y;    }

    void show() {
        System.out.println("Title: " + title + " | Cost: " + cost + " | Published year: " + yop);
    }
    }
    public static void main(String[] args) {
        Book defaultBook = new Book();
        defaultBook.show();

        Book customBook = new Book("Java Basics", 250);
        customBook.show();

        Book completeBook = new Book("Advanced Java", 500, 2026);
        completeBook.show();
    }
}

ERROR ::: at 19
 */