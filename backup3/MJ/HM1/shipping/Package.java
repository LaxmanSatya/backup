// File: Package.java (Assume this belongs to a package named 'shipping')
package HM1.shipping;

public class Package {
    // Fields with 4 different access specifiers
    public String destination;     // Accessible everywhere
    protected double weight;       // Accessible in same package and subclasses
    int daysToDeliver;             // Default (package-private): Accessible only in same package
    private String trackingId;     // Private: Accessible ONLY within this class

    public Package(String destination, double weight, int daysToDeliver, String trackingId) {
        this.destination = destination;
        this.weight = weight;
        this.daysToDeliver = daysToDeliver;
        this.trackingId = trackingId;
    }

    public void printLabel() {
        System.out.println("--- Package Label ---");
        System.out.println("Destination: " + destination);
        System.out.println("Weight: " + weight + " kg");
        System.out.println("Days: " + daysToDeliver);
        System.out.println("Tracking ID: " + trackingId); // Private is accessible here
    }
}
