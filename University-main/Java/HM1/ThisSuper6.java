package HM1;

class Parent {
    String message = "Parent Class Variable";

    void display() {
        System.out.println("Executing Parent display() method");
    }
}

class Child extends Parent {
    String message = "Child Class Variable"; // Shadows the parent variable

    @Override
    void display() {
        System.out.println("Executing Child display() method");
    }

    void demonstrateKeywords() {
        // --- USING 'this' KEYWORD (Refers to the current class instance) ---
        System.out.println("Using 'this.message': " + this.message);
        System.out.print("Using 'this.display()': ");
        this.display(); 

        System.out.println("--------------------------------------");

        // --- USING 'super' KEYWORD (Refers to the immediate parent class instance) ---
        System.out.println("Using 'super.message': " + super.message);
        System.out.print("Using 'super.display()': ");
        super.display(); 
    }
}

public class ThisSuper6 {
    public static void main(String[] args) {
        Child childObj = new Child();
        childObj.demonstrateKeywords();
    }
}

