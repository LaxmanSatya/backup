// File 3: Diffpackchild.java (in package_two)
package package_two;

import package_one.Parent;

public class Diffpackchild extends Parent {

    public void testVisibility() {
        System.out.println("Running from Child (package_two)");

        // 1. public -> Accessible everywhere
        System.out.println("publicVar: " + publicVar);

        // 2. protected -> Accessible because Child inherits from Parent
        System.out.println("protectedVar: " + protectedVar);

        // 3. default -> COMPILE ERROR (blocked across packages)
        // System.out.println(defaultVar);

        // 4. private -> COMPILE ERROR (blocked outside Parent class)
        // System.out.println(privateVar);
    }

    // Main method added to execute File 3 directly
    public static void main(String[] args) {
        Diffpackchild c = new Diffpackchild();
        c.testVisibility();
    }
}
