package HM1;

class StaticTest {
    static void sample() { System.out.println("Hello"); }
}

public class Problem10_StaticMethod {
    public static void main(String[] args) {
        StaticTest.sample(); // No object created
    }
}
