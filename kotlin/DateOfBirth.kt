// Example 6: DateOfBirth.java
data class Day(val d: Int) {
    init {
        check(0 < && <= 31, . toString () + ": day of month out of range")
    }
}

data class Month(val m: Int) {
    init {
        check(0 < && <= 12, . toString () + ": month out of range")
    }
}

data class Year(val y: Int) {
    init {
        check(1900 < && <= 2022, . toString () + ": year out of range")
    }
}

data class BirthDate(val month: Month, val day: Day, val year: Year)

fun main() {
    System.out.println(BirthDate(Month(7), Day(8), Year(1957)))
    System.out.println(BirthDate(Month(0), Day(32), Year(1857)))
}
