// Example 2: DistributedTypeValidation.java

class OneToTen {
    int val;
    OneToTen(int val) {
        this.val = val;
    }
    @Override
    public String toString() {
        return "OneToTen(" + val + ")";
    }
}

public class DistributedTypeValidation {
    static OneToTen f1(OneToTen x) {
        Check.validity(0 < x.val && x.val <= 10, x.val + " out of range");
        return new OneToTen(x.val * 10);
    }
    static OneToTen f2(OneToTen x) {
        Check.validity(0 < x.val && x.val <= 10, x.val + " out of range");
        return new OneToTen(x.val + 10);
    }
    public static void main(String[] args) {
        var a = new OneToTen(6);
        System.out.println(a);
        System.out.println(f1(a));
        System.out.println(f2(a));
        var b = new OneToTen(11);
        System.out.println(f1(b));
        a.val = 99;
        System.out.println(f2(a));
    }
}
