// Example 1: CheckedInt.java

public class CheckedInt {
    static int f1(int oneToTen) {
        Check.validity(0 < oneToTen && oneToTen <= 10, oneToTen + " out of range");
        return oneToTen * 10;
    }
    static int f2(int oneToTen) {
        Check.validity(0 < oneToTen && oneToTen <= 10, oneToTen + " out of range");
        return oneToTen + 10;
    }
    public static void main(String[] args) {
        int a = 6;
        System.out.println(a);
        System.out.println(f1(a));
        System.out.println(f2(a));
        int b = 11;
        System.out.println(f1(b));
        a = 99;
        System.out.println(f2(a));
    }
}
