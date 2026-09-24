class Stud {
 String id,name;
int age,marks;
}

public class Xencapdemo {
    public static void main(String[] args) {
            Stud s1=new Stud();
            s1.id="2500012345";
            s1.name="AAAAAAA";
            s1.age=25;
            s1.marks=550;
            System.out.println(s1.id+" "+s1.name+" "+s1.age+" "+s1.marks);
            Stud s2=new Stud();
            s2.id="2500012346";
            s2.name="BBBBBB"; /// example name (me_my ::: but, it also wrong name)
            s2.age=250;
            s2.marks=5500; /// wrong data
            System.out.println(s2.id+" "+s2.name+" "+s2.age+" "+s2.marks);
    }
}