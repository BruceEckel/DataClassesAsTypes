// Example 2: DistributedTypeValidation.java

data class OneToTen(var ott: Int) {
    override fun toString(): String {
        return "OneToTen($ott)"
    }
}

fun f1(x: OneToTen): OneToTen {
    check(0 < x.ott && x.ott <= 10, x.ott.toString() + " out of range")
    return OneToTen(x.ott * 10)
}

fun f2(x: OneToTen): OneToTen {
    check(0 < x.ott && x.ott <= 10, x.ott.toString() + " out of range")
    return OneToTen(x.ott + 10)
}

fun main() {
    val a = OneToTen(6)
    System.out.println(a)
    System.out.println(f1(a))
    System.out.println(f2(a))
    val b = OneToTen(11)
    System.out.println(f1(b))
    a.ott = 99
    System.out.println(f2(a))
}
