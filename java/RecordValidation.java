// Example 4: RecordValidation.java
// JDK 16 Records

record OneToTen(int val) {
    OneToTen {
        Check.validity(0 < val && val <= 10, val + " out of range");
    }
}

public class RecordValidation {
    static OneToTen f1(OneToTen x) {
        return new OneToTen(x.val() * 10);
    }
    static OneToTen f2(OneToTen x) {
        return new OneToTen(x.val() + 10);
    }
    public static void main(String[] args) {
        var a = new OneToTen(6);
        System.out.println(a);
        System.out.println(f1(a));
        System.out.println(f2(a));
        var b = new OneToTen(11);
        System.out.println(f1(b));
        // a.val = 99;  // Can 't modify val
    }
}
