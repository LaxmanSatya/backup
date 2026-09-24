public class ExeFlow {
    // Static variable
    static int staticVar = initStaticVar();

    // Static block

    // Instance variable
    int instanceVar = initInstanceVar();

    // Constructor
    ExeFlow() {
        System.out.println("Constructor executed");
    }
    // Instance block
    {
        System.out.println("Instance block executed");
    }

    // Helper methods
    static int initStaticVar() {
        System.out.println("Static variable initialized");
        return 10;
    }

    int initInstanceVar() {
        System.out.println("Instance variable initialized");
        return 20;
    }
    /* Any Where Put Static Block in A Class there Execute before Instances(block, vaiables) */
    static {
        System.out.println("Static block executed");
    }

    public static void main(String[] args) {
        System.out.println("Main method started"); /// static first
        System.out.print("\n");
        new ExeFlow();
    }
}

/* Flow

statics
instances
constructions

*/
