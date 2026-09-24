package Partice.PartBin;
/* Strong Association(Compostion) in Java Only */

/*
What is meant by  Composition...?

classes are Stongly Associated.

What About Aggrigation...?

classes are Weekly Associated.

Associated means...?

RelationShip Between Classes and dependency also lifespam

*/

/// EXample,

class Engine {
    String type;

    Engine(String type){
        this.type = type;
    }

    void start() {
        System.out.println(type + " engine started.");
    }
}

class Car {
    private final Engine engine; /// Composition Engine IS Owned By Car.

    Car(String type){
            this.engine = new Engine(type);
    }

    void startCar(){
        engine.start();
        System.out.println("Car is Moving .....");
    }
}

public class MainForComposition{ /// Strong Associated.
    public static void main(String[] args) {
        Car car = new Car("V6 Turbo ");
        car.startCar();
    }

}