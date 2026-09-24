package MS;

class name{
        /* [NOTER] ::: Java implicitly calls the default constructor if no explict constructor is defined. defaultly creates and call when class instance calls
         */
        /// no-arg constructor
        String letter_char1, latter_char2;
        name() /// no-Arg Constructor
        {
        this("i", "q");
        }
        name(String l1, String l2)
        {
            this(l1, l2, "z");
        }
        name(String l1, String l2, String l3)
        {
            this(l1, l2, l3, "y");
        }
        name(String l1, String l2, String l3, String l4)
        {
            System.out.println("Currently no doing.....");
        }
}

/// implementing Constructor Chaining in Oject oriented programming
public class s1_Constructors {

    public static void main(String[] args)
    {
        /// new memory giving to compiler tocreate a class instance(object)
        /// for value storing and working in virtual memory class structure in Java like declare, define of members and member functions. 
        name obj = new name(); 
        obj.letter_char1 = "i";
    }
}
