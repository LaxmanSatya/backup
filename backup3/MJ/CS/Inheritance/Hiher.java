package MJ.CS.Inheritance;

/***
 *****Hierarical One Super class More Childs.
*/
/// Important when working with same template. that template diferently perform action by which Class called.
///
/// 
/// Normal hierarical

// parent class (super)
class Animal{
    void eat(){
        System.out.println("Animal is Eating.");
    }
}

// child1 (sub_class1)
class Dog extends Animal{
    /// this constructor no action do...
    void Bark()
    {
        System.out.println("Dog bark Boow! Boow!");
    }
}
/// child2 (sub_class2)
class Cat extends Animal{
    void Meow(){
        System.out.println("Cat Meow! Meow!");
    }
}

public class Hiher {
    public static void main(String args[]){
        /// Now Create 2 Childs Instance Objects
        /// using class name to call static method
        /// Parent also a static memeber to assign by child classes. 
        Dog dog = new Dog();
        Cat cat = new Cat(); 
        dog.eat();
        cat.eat();
    }
}




