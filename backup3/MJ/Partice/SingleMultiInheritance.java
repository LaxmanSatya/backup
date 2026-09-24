
/// Inheritance is oops Things and "is-a" relationship  maintain in between classes.
/*Example ,

Ways Of Inheritance Implement

Single,
multilevel
hybrid
hierarical
multiple

*/

class Animal{
    void eat(){
        System.out.println("Eating...");
    }
}

/// single level
class Dog extends Animal{
    void bark(){
        System.out.println("!barking...");
    }
}

/// multi-level
class Puppy extends Dog {
    void weep() {
        System.out.println("weeping..!...!...");
    }
}


public class SingleMultiInheritance{
    public static void main(String args[]){
        /// Weekly Asscoation
        Puppy py = new Puppy();
        py.eat();
        py.bark();
        py.weep();
    }
}