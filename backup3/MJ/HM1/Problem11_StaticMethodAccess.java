package HM1;

class DisplayDemo {
    static void display() { System.out.println("Welcome message"); }
}

public class Problem11_StaticMethodAccess {
    public static void main(String[] args) {
        DisplayDemo.display(); // Called directly
    }
}
