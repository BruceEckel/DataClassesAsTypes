// Example 1: CheckedInt.kt

fun f1(oneToTen: Int): Int {
    check(0 < oneToTen && oneToTen <= 10, "$oneToTen out of range")
    return oneToTen * 10
}

fun f2(oneToTen: Int): Int {
    check(0 < oneToTen && oneToTen <= 10, "$oneToTen out of range")
    return oneToTen + 10
}

fun main() {
    var a = 6
    System.out.println(a)
    System.out.println(f1(a))
    System.out.println(f2(a))
    val b = 11
    System.out.println(f1(b))
    a = 99
    System.out.println(f2(a))
}
