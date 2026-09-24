package HM1;

class User {
    String name;
    int age;

    // Constructor 1: Takes only name
    public User(String name) {
        this.name = name;
        this.age = 0; // Default value if age is not provided
    }

    // Constructor 2: Takes name and age
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class ConstOverload2 {
    public static void main(String[] args) {
        // Accessing the first constructor
        User user1 = new User("Alice");
        
        // Accessing the second constructor
        User user2 = new User("Bob", 21);

        user1.displayInfo();
        user2.displayInfo();
    }
}
