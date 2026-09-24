package HM1;

class Test {
    // Default constructor
    public Test() {
        System.out.println("I am default");
    }

    // Parameterized constructor
    public Test(int length, int breadth) {
        // Invoking the default constructor using this()
        // Note: this() must be the very first statement in a constructor
        this(); 
        
        int multiplication = length * breadth;
        System.out.println("Multiplication value: " + multiplication);
    }
}

public class ConstChain4 {
    public static void main(String[] args) {
        // Instantiating the class using the parameterized constructor
        new Test(5, 10);
    }
}
