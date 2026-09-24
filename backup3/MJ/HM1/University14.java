package HM1;

public class University14 {
    // Static field: Shared by all objects of this class
    public static int totalStudents = 0;

    // Instance field: Each individual student object gets its own copy
    public String studentName;

    // Constructor to initialize a new student
    public University14(String name) {
        this.studentName = name;
        // Increment the total student count whenever a new object is created
        totalStudents++; 
    }

    public static void main(String[] args) {
        // Create individual student objects
        University14 student1 = new University14("Alice");
        University14 student2 = new University14("Bob");
        University14 student3 = new University14("Charlie");

        // Print instance fields (unique to each object)
        System.out.println("Student 1 Name: " + student1.studentName);
        System.out.println("Student 2 Name: " + student2.studentName);

        System.out.println("Student 3 Name: " + student3.studentName);

        // Print static field (shared by the entire class)
        System.out.println("Total Students in University: " + University14.totalStudents);
    }
}
