package HM1;

// File: Main.java (Located in a DIFFERENT package to show access boundaries)
import HM1.shipping.Package;

public class Package5 {
    public static void main(String[] args) {
        Package pkg = new Package("New York", 12.5, 3, "TRK12345");
        
        // 1. Calling the public method works fine
        pkg.printLabel();
        
        // 2. Testing direct field accessibility from an external class:
        System.out.println(pkg.destination); // WORKS: 'public' is open to all packages.
        
        // System.out.println(pkg.weight);    // ERROR: 'protected' field not visible outside package.
        // System.out.println(pkg.daysToDeliver); // ERROR: 'default' field not visible outside package.
        // System.out.println(pkg.trackingId); // ERROR: 'private' field is completely hidden.
    }
}

