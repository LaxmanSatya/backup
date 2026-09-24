// File 2: SamePackageTest.java (in package_one)
package package_one;

public class SamePackageTest {
    public static void main(String[] args) {
        Parent p = new Parent();

        System.out.println("Public var : "+p.publicVar);    // OK: public
        System.out.println("Protected Var : "+p.protectedVar); // OK: same package
        System.out.println("Default var : "+p.defaultVar);   // OK: same package

        // (not visible)
        // System.out.println(p.privateVar); // ERROR: private is blocked 
        p.showPrivate();                    // OK: calls public method
    }
}