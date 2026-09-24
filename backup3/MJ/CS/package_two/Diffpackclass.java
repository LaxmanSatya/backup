// File 4: Difpackclass.java (in package_two)
package package_two;

import package_one.Parent;

public class Diffpackclass {

    public void testVisibility() {
        System.out.println("Running from individual class from a different Package  (package_two) ");
        Parent p = new Parent();

        // 1. public -> Accessible via object reference
        System.out.println("publicVar: " + p.publicVar);

        // 2. protected -> COMPILE ERROR (Check is NOT a subclass)
        // System.out.println(p.protectedVar);

        // 3. default -> COMPILE ERROR (blocked across packages)
        // System.out.println(p.defaultVar);

        // 4. private -> COMPILE ERROR (blocked outside Parent class)
        // System.out.println(p.privateVar);
    }

    // Main method added to execute File 4 directly
    public static void main(String[] args) {
        Diffpackclass ch = new Diffpackclass();
        ch.testVisibility();
    }
}
