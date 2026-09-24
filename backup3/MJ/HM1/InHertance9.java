package HM1;

class Person {
    // Default constructor of Parent class
    public Person() {
        System.out.println("I am Person constructor");
    }
}

class Student extends Person {
    // Default constructor of Child class
    public Student() {
        // super(); is implicitly added here by the Java compiler
        System.out.println("I am student constructor");
    }
}

public class InHertance9 {
    public static void main(String[] args) {
        // Invoking only the student class instantiation
        new Student();
    }
}
