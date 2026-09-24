package HM1;

class Demo {
    // Method 1: No parameters
    void display() {
        System.out.println("display() method called with no parameters.");
    }

    // Method 2: One integer parameter (Overloaded method)
    void display(int a) {
        System.out.println("display(int a) method called with value: " + a);
    }
}

public class CompileTimePolyMethOverload7 {
    public static void main(String[] args) {
        Demo obj = new Demo();
        
        // Invoking both methods to show they behave differently based on arguments
        obj.display();
        obj.display(10);
    }
}

