package HM1;

class BankConfig {
    static double interestRate;
    static {
        interestRate = 4.5;
        System.out.println("Static block executed");
    }
    public BankConfig() { System.out.println("Account Created"); }
}

public class Problem13_StaticBlock {
    public static void main(String[] args) {
        new BankConfig();
        new BankConfig();
        new BankConfig();
        System.out.println("Interest Rate: " + BankConfig.interestRate);
    }
}

