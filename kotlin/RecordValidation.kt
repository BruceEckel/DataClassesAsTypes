// Example 4: RecordValidation.java
// JDK 16 Records

data class OneToTen(: Int) {
    init {
        check(0 < && <= 10, . toString () + " out of range")
    }
}

fun f1(x: OneToTen): OneToTen {
    return OneToTen(x.ott() * 10)
}

fun f2(x: OneToTen): OneToTen {
    return OneToTen(x.ott() + 10)
}

fun main() {
    val a = OneToTen(6)
    System.out.println(a)
    System.out.println(f1(a))
    System.out.println(f2(a))
    val b = OneToTen(11)
    System.out.println(f1(b))
    // a.ott = 99;  // Can 't modify ott
}
