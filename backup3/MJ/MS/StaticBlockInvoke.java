public class StaticBlockInvoke 
{
    static {
        System.out.print("Okay");
    }
    public static void main(String arguments[]) {
            new StaticBlockInvoke(); new StaticBlockInvoke(); new StaticBlockInvoke(); new StaticBlockInvoke(); new StaticBlockInvoke(); new StaticBlockInvoke();
    }
}