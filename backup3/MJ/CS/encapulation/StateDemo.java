class Counter {
    int instanceCount = 0;        // Instance state: separate copy per object
    static int classCount = 0;    // Class state: single shared copy for all objects

    void increment() {
        instanceCount++;
        classCount++;
    }
}

public class StateDemo {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        c1.increment();
        System.out.println("\n\nc1 instanceCount: " + c1.instanceCount+" c1 classCount: " + Counter.classCount); 

        c1.increment();
        System.out.println("\n\nc1 instanceCount: " + c1.instanceCount+" c1 classCount: " + Counter.classCount); 

        c2.increment();
        System.out.println("\n\nc2 instanceCount: " + c2.instanceCount+" c2 classCount: " + Counter.classCount); 

        c2.increment();
        System.out.println("\n\nc2 instanceCount: " + c2.instanceCount+" c2 classCount: " + Counter.classCount); 
    }
}
