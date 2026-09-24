public class StringComparisonDemo {
 public static void main(String[] args) {
 // Created in the String Constant Pool (shared memory)
 String s1 = "Java"; /// [NOW++] here implicitly refer same memory loaction of s1 and s2 for memory efficiency and memory optimization
 String s2 = "Java"; /// [NOW++] if data in differnt refernec are same is 2 reference only locate same memory. otherwise both referce different memory location.

 String s3 = new String("Java"); /// explicitly create a new memory for same data value
 String s4 = new String("Java"); /// we are asking new memrory location for same data. so both reference will point to different memory location.

System.out.println("Are s1 and s2 pointing same location: "+(s1 == s2));
System.out.println("Does data in s1 and s2 are same : "+s1.equals(s2));
System.out.println("Are s1 and s3 pointing same location: "+(s1 == s3));
System.out.println("Does data in s1 and s3 are same : "+s1.equals(s3));
System.out.println("Are s3 and s4 pointing same location: "+(s4 == s3));
System.out.println("Does data in s3 and s4 are same : "+s3.equals(s4));
 }
}