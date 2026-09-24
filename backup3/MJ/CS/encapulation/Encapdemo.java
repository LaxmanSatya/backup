class Stud {
    // 1. Private fields: Hiding internal state from direct outside access
    private String id;
    private String name;
    private int age;
    private int marks;

    // Parameterized constructor using setters to enforce validation during creation
    public Stud(String id, String name, int age, int marks) {
        setId(id);
        setName(name);
        setAge(age);
        setMarks(marks);
    }


    // SETTERS: Controlled Write Access with Validation Rules

    public void setId(String id) {
        if (id != null) {
            this.id = id;
        } else {
            System.out.println("Invalid ID provided.");
        }
    }

    public void setName(String name) {
        if (name != null) {
            this.name = name;
        } else {
            System.out.println("Invalid Name provided.");
        }
    }

    public void setAge(int age) {
        // Validation: Age must be between 1 and 100
        if (age >= 1 && age <= 100) {
            this.age = age;
        } 
else {
            System.out.println("Validation Error: Age " + age + " is invalid (Must be 1-100). Defaulting to 0.");
        }
    }

    public void setMarks(int marks) {
        // Validation: Maximum possible marks is 600
        if (marks >= 0 && marks <= 600) {
            this.marks = marks;
        } 
else {
            System.out.println("Validation Error: Marks " + marks + " is invalid (Must be 0-600). Defaulting to 0.");
        }
    }

    public void display() {
        System.out.println("ID: " + id + " | Name: " + name + " | Age: " + age + " | Marks: " + marks);
    }

}

public class Encapdemo {
    public static void main(String[] args) {
        System.out.println("1. Valid Student Record ");
        Stud s1 = new Stud("2500012345", "AAAAAAA", 25, 550);
        s1.display();

        System.out.println("\n 2. Invalid Student Record (Intercepted & Protected) ");
        // Setting age=250 and marks=5500 triggers validation errors instead of corrupting data
        Stud s2 = new Stud("2500012346", "BBBBBB", 250, 5500);
        s2.display();

        System.out.println("\n 3. Correcting Data via Setters ");
        s2.setAge(22);
        s2.setMarks(520);
        s2.display();
    }
}