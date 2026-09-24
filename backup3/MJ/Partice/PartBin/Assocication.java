package Partice.PartBin;
/// Association here we using the classes not extending but, simple using the container and compoents
/// 
/// *** here, main things lifespan& Dependency Strength
/// 
/// In 2 Ways to using class 
/// Composition
/// Aggregation
/// 
/// here, class is Container
///       class members are Compoents
/// 

/* Aggregation means 2 conatiner are weakly Asscociated(Related) one class don`t depenent another classs
This is relationship life span is depends on its own Conatiner 

Example, Mentor class(container) and StudentIdCard Container
*/
/* here  */
class Mentor {
    String name;
    Mentor(String name){
        this.name = name;
    }
}

class StudentIDCard {
    String cardNumber;
    StudentIDCard(String cardNumber) {
        this.cardNumber = cardNumber;
    }
}
/*
aggregation with student id card if univeristy not exist student is also not exists. it a Aggregation the the Container are Storngly Associated.

Strongly asscocication means one class highly depends on another class like student  id card -> university

This Asscoaction tells 2 container and components how Composied. and storly composition

This is called  Composition Association
*/

/*Composition means 2 container are stronly Asscociated(related) [or] one class fully depends on another class*/
class UniversityStudent{
    private StudentIDCard _idCard;
    String studentName;
    Mentor mentor;

    UniversityStudent(String studentName, String cardNumber, Mentor mentor) {
        this.studentName = studentName;
        this.mentor = mentor;
        this._idCard = new StudentIDCard(cardNumber); /// Instantiated directly inside the  student constructor.

    }
    public String getIdCardNumber() {
        return _idCard.cardNumber;
    }
}

public class Assocication {
public static void main(String[] args) {
    /*
    Association in Java is a structural relationship between two separate classes established through their objects, representing a uses-a, has-a, or knows-a connection where both classes maintain independent lifecycles.  It is implemented by using instance variables or parameters to create references between objects, allowing them to interact and exchange information without implying ownership or strict dependency. 
    */
}
}

