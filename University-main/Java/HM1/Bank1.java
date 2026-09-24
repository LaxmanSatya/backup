package HM1;

class Bank {
    // Private field cannot be accessed directly outside this class
    private double balance;

    // Setter method to modify the balance
    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        }
    }

    // Getter method to retrieve the balance
    public double getBalance() {
        return this.balance;
    }
}

public class Bank1 {
    public static void main(String[] args) {
        Bank account = new Bank();
        
        // Setting the balance using the setter
        account.setBalance(5000.75);
        
        // Getting the balance using the getter
        System.out.println("Bank Balance: $" + account.getBalance());
    }
}
