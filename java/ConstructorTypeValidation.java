// Example 3: ConstructorTypeValidation.java

class OneToTen {
    int val;
    OneToTen(int val) {
        this.val = val;
        Check.validity(0 < val && val <= 10, val + " out of range");
    }
    @Override
    public String toString() {
        return "OneToTen(" + val + ")";
    }
}

public class ConstructorTypeValidation {
    static OneToTen f1(OneToTen x) {
        return new OneToTen(x.val * 10);
    }
    static OneToTen f2(OneToTen x) {
        return new OneToTen(x.val + 10);
    }
    public static void main(String[] args) {
        var a = new OneToTen(6);
        System.out.println(a);
        System.out.println(f1(a));
        System.out.println(f2(a));
        var b = new OneToTen(11);
        System.out.println(f1(b));
        a.val = 99;   // Can still mutate to an invalid OneToTen
        System.out.println(a + ": Didn't detect that it's out of range!");
        // So, still need to validate OneToTen inside functions
        System.out.println(f2(a));
    }
}
