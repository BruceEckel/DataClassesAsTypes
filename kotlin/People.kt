// Example 5: People.java
data class FullName(: String?) {
    init {
        System.out.println("FullName checking " +)
        check(. split " ".length > 1, .toString()+" needs at least first and last names")
    }
}

data class BirthDate(: String?) {
    init {
        System.out.println("BirthDate checking " +)
        check(true, "Add code to validate " +)
    }
}

data class EmailAddress(: String?) {
    init {
        System.out.println("EmailAddress checking " +)
        check(true, "Add code to validate" +)
    }
}

data class Person(: FullName?, : BirthDate?, : EmailAddress?) {
    init {
        System.out.println("Person checking fields")
        check(true, "Add code to validate Person")
    }
}

fun main() {
    val person = Person(
        FullName("Bruce Eckel"),
        BirthDate("7/8/1957"),
        EmailAddress("mindviewinc@gmail.com")
    )
}
