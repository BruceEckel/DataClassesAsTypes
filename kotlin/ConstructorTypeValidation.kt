// Example 3: ConstructorTypeValidation.java
data class OneToTen(var ott: Int) {
    init {
        check(0 < ott && ott <= 10, "$ott out of range")
    }


    override fun toString(): String {
        return "OneToTen($ott)"
    }
}

fun f1(x: OneToTen): OneToTen {
    return OneToTen(x.ott * 10)
}

fun f2(x: OneToTen): OneToTen {
    return OneToTen(x.ott + 10)
}

fun main() {
    val a = OneToTen(6)
    System.out.println(a)
    System.out.println(f1(a))
    System.out.println(f2(a))
    val b = OneToTen(11)
    System.out.println(f1(b))
    a.ott = 99 // Can still mutate to an invalid OneToTen
    System.out.println("$a: Didn't detect that it's out of range!")
    // So, still need to validate OneToTen inside functions
    System.out.println(f2(a))
}
