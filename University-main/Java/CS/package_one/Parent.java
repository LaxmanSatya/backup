// File 1: Parent.java (in package_one)
package package_one;

public class Parent {
    private   int privateVar   = 10; // Only in Parent
              int defaultVar   = 20; // Only in package_one
    protected int protectedVar = 30; // In package_one + subclasses
    public    int publicVar    = 40; // Everywhere

    public void showPrivate() {
        // Accessible inside the class itself
        System.out.println("Private access through member method : " + privateVar);
    }
}
