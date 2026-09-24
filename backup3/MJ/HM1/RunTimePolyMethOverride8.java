package HM1; 

class Demo1 {
    void display() {
        System.out.println("display() inside Demo1 (Parent Class)");
    }
}

class Demo2 extends Demo1 {
    // Overriding the display method of Demo1
    @Override
    void display() {
        System.out.println("display() inside Demo2 (Child Class)");
    }

    void printBothMethods() {
        // Invokes child class version
        display(); 
        
        // Invokes parent class version
        super.display(); 
    }
}

public class RunTimePolyMethOverride8 {
    public static void main(String[] args) {
        // Invoke Demo2 from main
        Demo2 obj = new Demo2();
        obj.printBothMethods();
    }
}
