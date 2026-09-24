package HM1;

class Square {
    // Attribute of the Square class
    int side;

    public Square(int side) {
        this.side = side;
    }
}

class Demo {
    // Parameterized constructor that accepts a Square object
    public Demo(Square s) {
        // Accessing the attributes of the Square class instance
        System.out.println("Square side length accessed inside Demo: " + s.side);
        System.out.println("Calculated Area inside Demo: " + (s.side * s.side));
    }
}

public class PassObjectsConst3 {
    public static void main(String[] args) {
        // Create an instance of the Square class
        Square squareObj = new Square(5);
        
        // Pass the square instance into the Demo constructor
        new Demo(squareObj);
    }
}
