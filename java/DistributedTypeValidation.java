// Example 2: DistributedTypeValidation.java

class OneToTen {
    int ott;
    OneToTen(int ott) {
        this.ott = ott;
    }
    @Override
    public String toString() {
        return "OneToTen(" + ott + ")";
    }
}

public class DistributedTypeValidation {
    static OneToTen f1(OneToTen x) {
        Check.validity(0 < x.ott && x.ott <= 10, x.ott + " out of range");
        return new OneToTen(x.ott * 10);
    }
    static OneToTen f2(OneToTen x) {
        Check.validity(0 < x.ott && x.ott <= 10, x.ott + " out of range");
        return new OneToTen(x.ott + 10);
    }
    public static void main(String[] args) {
        var a = new OneToTen(6);
        System.out.println(a);
        System.out.println(f1(a));
        System.out.println(f2(a));
        var b = new OneToTen(11);
        System.out.println(f1(b));
        a.ott = 99;
        System.out.println(f2(a));
    }
}
