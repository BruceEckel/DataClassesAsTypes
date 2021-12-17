public class Check {
    public static void validity(Boolean exp, String errMsg) {
        if(!exp) {
            System.out.println("Type failure: " + errMsg);
        }
    }
}
