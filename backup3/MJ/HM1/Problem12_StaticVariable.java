package HM1;

class ValueCounter {
    static int count = 0;
    public ValueCounter() { count++; }
    static void increment() { count++; }
}

public class Problem12_StaticVariable {
    public static void main(String[] args) {
        new ValueCounter();
        new ValueCounter();
        ValueCounter.increment();
        ValueCounter.increment();
        System.out.println("Final count: " + ValueCounter.count); // Prints 4
    }
}
